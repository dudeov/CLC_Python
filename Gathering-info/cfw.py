import paramiko
import time
import getpass
import os
from host_efw_undone import efw
from host_efw_undone import cfw
from host_efw_undone import name

paramiko.util.log_to_file("filename.log")

UN = raw_input("Username : ")
PW = getpass.getpass("Password: ") 

# This loop get IPs of CFWs and EFW and does double SSH from CFW to EFW
for cfw_ip, hn in  zip(cfw, name):
    print cfw_ip
    print hn

    buf = '' 
    output = ''
	
    try:
         twrssh = paramiko.SSHClient()
         twrssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
         twrssh.connect(cfw_ip, port=22, username=UN, password=PW)
         print "Connected sucessfully to %s" % hn
    except paramiko.AuthenticationException:
        print "Authentication failed when connecting to %s. Going to next site." % hn
        continue
    except:
        print "Could not SSH to %s, waiting for it to start. Going to next site" % hn
        continue

    remote = twrssh.invoke_shell()
    time.sleep(2)

    output = remote.recv(65000)
	
# This 'if' checks if we are in the BSD shell or in CLI

    if output.endswith(('% ', '%\t')):
        print('In shell')
        remote.send('cli show chassis hardware "|" match Chassis \n')
        time.sleep(6)
        buf = remote.recv(65000)
    elif output.endswith('> '):
        print('In CLI')
        remote.send('show chassis hardware | match Chassis \n')
        time.sleep(6)
        buf = remote.recv(65000)
    else:
        print ('NO PROMT!, next loop')
        continue
	
	
    twrssh.close() 

    
    fn = 'CLC_output.txt'
    f = open(fn, 'a')
    f.write(hn)
    f.write(buf)
    f.close()


    
