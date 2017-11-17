#!/usr/bin/env python3
import pexpect
import getpass
import os
import time
import d_list
import sys
import re
#######################################     get_sysargv()      #################################

def get_sysargv():

  if len(sys.argv)<2:
    print('Please, specify at least one FWs hostname as an argument. Example: ./get_logs.py LB3-CFW')
    sys.exit(1)
  elif len(sys.argv)>=2 and sys.argv[1] in d_list.devices:
    UN = 'cne'
#    PW = getpass.getpass("Password for %s: "% UN)
    PW = 'T@c@cs1sD0wn!'
    device_cred = {'device_hn': sys.argv[1], 'device_ip': d_list.devices[sys.argv[1]], 'device_un': UN, 'device_pw': PW}
    print('#'*30)
    print('Working with %s, %s' % (sys.argv[1], d_list.devices[sys.argv[1]] ))
  else:
    print('No match, specify a correct FWs hostname as an argument. Example: ./get_logs.py LB3-CFW')
    sys.exit(1)
  return device_cred

##################################################################################################
#########################################        tgz_logs         ################################
def tgz_logs(device_cred):
  print('#'*30)
  time_str = time.strftime('%Y-%m-%d_%H-%M', time.localtime())  

  child = pexpect.spawn('ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no ' + device_cred['device_un'] + '@' + device_cred['device_ip'])
  try:  
    child.expect('Password:')
    child.sendline(device_cred['device_pw'])
    user_at_host_string = device_cred['device_un'] + '@' + device_cred['device_hn']
    child.expect(user_at_host_string)
######### which is Primary? ####################
    if re.search(r'{primary:node([0-1])}', str(child.before)):
      node_num = re.search(r'{primary:node([0-1])}', str(child.before)).group(1)
    else:
      print("don't see the prompts, exiting")
      sys.exit(1)
    if node_num == '0':
      prim_node = 'node0'
      sec_node = 'node1'
    elif node_num == '1':
      prim_node = 'node1'
      sec_node = 'node0'
    else:
      print("don't recoznize the node num, exiting")
      sys.exit(1)
    print("Primary node is {}".format(prim_node))
    print('#'*30)
######### which is Primary? ####################
    fn_sec = device_cred['device_hn'] + '_var_log_' + sec_node + '_' + time_str + '.tgz'
    fn_prim = device_cred['device_hn'] + '_var_log_' + prim_node + '_' + time_str + '.tgz'
    any_node = 'node*'
    fn_scp = device_cred['device_hn'] + '_var_log_' + any_node  + '_' + time_str + '.tgz'
    child.sendline('file archive compress source /var/log/ destination /var/tmp/' + fn_prim)
    child.expect(user_at_host_string)
    child.sendline('start shell')
    child.expect('%')
    try:  
      child.sendline('rlogin -T ' + sec_node)
      child.expect('secondary', timeout = 5)
      child.sendline('file archive compress source /var/log/ destination /var/tmp/' + fn_sec)
      child.expect('secondary')
      child.sendline('file copy /var/tmp/' + fn_sec + ' ' + prim_node + ':/var/tmp/')
      child.expect('secondary')
      return fn_prim, fn_sec, fn_scp
    except:
      print('########\nException was raised\nSecondary is unavailable!\n###########')
      return fn_prim, fn_sec, fn_scp
  except Exception as var:
    print(var)
    print('Exception was raised!')
    sys.exit(1)

################################################################################################

########################    get_logs! #####################

def get_logs(fn_prim, fn_sec, fn_scp, device_cred):
  dird = device_cred['device_hn']
####  creating directory #####
  if not os.path.exists(dird):
    os.mkdir(dird)
#############################
  dest_path = device_cred['device_un'] + '@' + device_cred['device_ip'] + r':/var/tmp/'
  scp_str = 'scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no ' + dest_path +  fn_scp + r' ./' + dird
#  scp_str = 'scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no ' +  device_cred['device_un'] + '@' + device_cred['device_ip'] + ':/var/tmp/' + fn_prim + r' ./' + dird
  print(scp_str)
  print('#'*30)
  child = pexpect.spawn(scp_str)
  try:
    child.expect('Password:')
    child.sendline(device_cred['device_pw'])
    child.expect([pexpect.TIMEOUT, pexpect.EOF], timeout = 900)
    download_str = str(child.before)[2:-1]
    down_str_tmp = re.sub(r'\\r\\n\\r', '\n', download_str)
    down_str_pretty = re.sub(r'\\r', '\n', down_str_tmp)
    print(down_str_pretty)
    ls_str = 'ls -l ' + dird + ' | grep "' + fn_prim + r'\|' + fn_sec + '"'
    print('#'*30)
    print(ls_str)
    print('#'*30)
    os.system(ls_str)
  except Exception as var:
    print(var)
    print('Exception was raised!')
    sys.exit(1)  
  

if __name__ == '__main__':
  device_cred = get_sysargv()
  fn_prim, fn_sec, fn_scp = tgz_logs(device_cred)
  get_logs(fn_prim, fn_sec, fn_scp, device_cred)
