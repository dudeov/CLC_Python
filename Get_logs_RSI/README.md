Example

```
./get-logs.py LB3-EFW
##############################
Working with LB3-EFW, 10.225.32.117
##############################
Primary node is node0
##############################
scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no cne@10.225.32.117:/var/tmp/LB3-EFW_var_log_node*_2017-11-17_19-51.tgz ./LB3-EFW
##############################

LB3-EFW_var_log_node0_2017-11-17_19-51.tgz      0%    0     0.0KB/s   --:-- ETA
LB3-EFW_var_log_node0_2017-11-17_19-51.tgz     60%  672KB 672.0KB/s   00:00 ETA
LB3-EFW_var_log_node0_2017-11-17_19-51.tgz    100% 1118KB 714.2KB/s   00:01
LB3-EFW_var_log_node1_2017-11-17_19-51.tgz      0%    0     0.0KB/s   --:-- ETA
LB3-EFW_var_log_node1_2017-11-17_19-51.tgz    100%  156KB 716.3KB/s   00:00
\n
##############################
ls -l LB3-EFW | grep "LB3-EFW_var_log_node0_2017-11-17_19-51.tgz\|LB3-EFW_var_log_node1_2017-11-17_19-51.tgz"
##############################
-rw------- 1 root root 1144697 Nov 17 19:51 LB3-EFW_var_log_node0_2017-11-17_19-51.tgz
-rw------- 1 root root  159881 Nov 17 19:51 LB3-EFW_var_log_node1_2017-11-17_19-51.tgz
```

Directory will be created if doesn't exist
