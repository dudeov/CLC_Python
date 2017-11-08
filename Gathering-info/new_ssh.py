#!/usr/bin/env python

import paramiko
import getpass
import os
import time

paramiko.util.log_to_file("filename.log")

UN = 'achuvakov'
PW = getpass.getpass("Password for %s: "% UN) 
UN = 'achuvakov'


fn = raw_input("Enter name of the destination file: ")
try: os.remove(fn)
except: pass

dd = {'dev1': '172.28.5.1', 'dev2': '172.28.5.2'}

my_Commamd = raw_input("Which command? Type here: ")

for i in dd:
  with paramiko.SSHClient() as client:

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  
    try:
      client.connect(hostname=dd[i], username= UN, password= PW)
      print 'Connected to {}'.format(i)

    except Exception as var:
      print 'Something is wrong with {}: {}\n Going to next loop'.format(i, var)
      continue

  
    stdin, stdout, stderr = client.exec_command(my_Commamd)
    with open(fn, 'a') as f:
      f.write('\n{}> {}\n'.format(i, my_Commamd))
      f.write(stdout.read())
      f.write(stderr.read())
      f.close()
