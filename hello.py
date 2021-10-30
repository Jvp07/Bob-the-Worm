import os
import sys
import threading
import nmap
import subprocess
import paramiko
import main
#help="""---------------- HOST SCAN ---------------
#	python hello.py [options]
#	options -s startip
#	options -e endip
#	EX . python hello.py -s 10.1.1.0 -e 10.1.1.225
#	"""

if len(sys.argv)!=5:
	print(help)
	sys.exit(0)

IpList = []





def nmaper():
    portscan = nmap.PortScanner()
    #startport = 1
    #endport = 1023
    portnum = 22
    for ips in IpList:
        #for portnum in range (startport, endport + 1):
        portscan.scan(ips, str(portnum))
        portscan = portscan['scan'][ips]['tcp'][portnum]['state']
        print(f'port {portnum} is {portscan}.')
    #once all open ports have been found
        if portscan == 'open':
            yes = "yes"
        #    subprocess.run(["ssh", "msfadmin@"+ips])\
    command = 'ls'
    client = paramiko.SSHClient()
    client.connect('192.168.56.103', username='msfadmin', password='msfadmin')
    (stdin, stdout, stderr) = client.exec_command(command)
    lines = stdout.readlines()
    print(lines)

    client.close()



def ping(ip):
    
    #x = 0
    if not os.system('ping '+ip+' >'+ip):
        print(ip)
        #while ("yes" == "yes"):
         #   IpList[x] += ip
         #   x +=1
        IpList.append(ip)
        #print(IpList)
    os.system('del '+ip)
#print(IpList)
#startip=list(map(int,sys.argv[sys.argv.index('-s')+1].strip().split('.')))
#endip=list(map(int,sys.argv[sys.argv.index('-e')+1].strip().split('.')))

#print(IpList)
def scanner():  
    while startip != endip:
#    ping(startip)
    
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
    nmaper()


#nmaper()
def counter():
    x = 0 
    while (x < 100):
        print(x)
        x +=1



        
#print(IpList)