import paramiko
import time
import getpass
import os
from host_efw import efw
from host_efw import cfw
from host_efw import name


UN = raw_input("Username : ")




# This loop get IPs of CFWs and EFW and does double SSH from CFW to EFW
for cfw_ip, efw_ip, hn in  zip(cfw, efw, name):
    print cfw_ip
    print efw_ip
    print hn
    PW = getpass.getpass("Password: ")
   
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

    if buf1.endswith("Are you sure you want to continue connecting (yes/no)? "):
        remote.send('yes \n')
        time.sleep(2)
        print('Got in 1-st if in EFW')
        buf2 = remote.recv(6500)
        if buf2.endswith("Password:"):
           remote.send('%s\n' % PW)
           output1 = remote.recv(65000)           
           print('I am in 2-nd if in EFW')
    elif buf1.endswith("Password:"):
        remote.send('%s\n' % PW)
        time.sleep(2)
        output1 = remote.recv(65000)        
        print('I am in elif in EFW')
    else:
        print('Stuck in else/no prooper invitation in EFW - starting next loop')
        continue

# This 'if' checks if we are in the BSD shell or in CLI

    if output1.endswith(('% ', '%\t')):
        remote.send('cli \n')
        print('sent cli on CFW')

    elif output1.endswith('> '):
        print('Already in CLI on CFW')
    else:
        print ('NO PROMT!, next loop')
        continue

    remote.send('show chassis hardware | display xml | no-more \n')
    time.sleep(3)
    buf = remote.recv(65000)

    remote.send('exit\n')
    remote.send('exit\n')
    remote.send('exit\n')

    twrssh.close() 

    f = open('EFW_output.txt', 'a')
    f.write(buf)
    f.close()


    
