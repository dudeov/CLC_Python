

import paramiko
import getpass
import os


paramiko.util.log_to_file("filename.log")


PW = getpass.getpass("Password: ") 

fn = raw_input("Enter name of the destination file: ")
try: os.remove(fn)

d = {'SG1_MX1': '10.225.128.1','SG1_MX2': '10.225.128.2'}


for i in d:
  client = paramiko.SSHClient()
  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  client.connect(hostname=d[i], username= 'alex.chuvakov', password= PW)
  stdin, stdout, stderr = client.exec_command('cli')
  print stdout.read()
  client.close()
