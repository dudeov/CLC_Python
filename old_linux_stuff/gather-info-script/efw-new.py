import paramiko
import time
import getpass
import os
import re
from host_efw_undone import efw
from host_efw_undone import cfw
from host_efw_undone import name


UN = raw_input("Username : ")
PW = getpass.getpass("Password: ")



# This loop get IPs of CFWs and EFW and does double SSH from CFW to EFW
for cfw_ip, efw_ip, hn in  zip(cfw, efw, name):
    print cfw_ip
    print efw_ip
    print hn
#    PW = getpass.getpass("Password: ")
   
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

    output = ''
    buf2 = ''
    buf1 = ''
    buf = ''
    output1 = ''

    remote = twrssh.invoke_shell()
    output = remote.recv(65000)

    remote.send('ssh %s@%s \n' % (UN, efw_ip))    
    time.sleep(2)
    buf1 = remote.recv(65000)



# Trying to take all cases into consideration

    if re.search('\s*Are you sure you want to continue connecting (yes/no)?\s*',buf1):
        remote.send('yes \n')
        time.sleep(2)
        print(' Are you sure you want to continue connecting (yes/no)? ')
        buf2 = remote.recv(6500)
        if re.search('\s*assword\s*',buf2):
           remote.send('%s\n' % PW)
           output1 = remote.recv(65000)           
           print(' Password after adding to trust hosts')
    elif re.search('\s*assword\s*',buf1): 
        remote.send('%s\n' % PW)
        time.sleep(2)
        output1 = remote.recv(65000)        
        print(' Password from 1-st attempt ')
    else:
        print('Stuck in else/no Password invitation in EFW - starting next loop')
        continue

# This 'if' checks if we are in the BSD shell or in CLI

    if output1.endswith(('% ', '%\t')):
        print('In shell')
        remote.send("cli show version node 0 \n")
        time.sleep(2)
#        remote.send('cli show chassis cluster interfaces "|" match em \n')
#        time.sleep(2)
        buf = remote.recv(65000)
    elif output1.endswith('> '):
        print('In CLI on CFW')
        remote.send('show version node 0 \n')
        time.sleep(2)
#        remote.send('show chassis cluster interfaces | match em \n')
#        time.sleep(3)
        buf = remote.recv(65000)
    else:
        print ('NO PROMT!, next loop')
        continue


    remote.send('exit\n')
    remote.send('exit\n')
    remote.send('exit\n')

    twrssh.close() 

#    fn = 'CFW-' + hn + '.txt'
    fn = 'CLC_efw_sh_ver.txt.txt'

    f = open(fn, 'a')

    f.write(buf)
    f.close()


    
