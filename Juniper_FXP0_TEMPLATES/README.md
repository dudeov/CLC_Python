#How to use prender.py


Type "python prender.py file.yml file.j2" and you'll get the output on your screen

Note. Order of .yml and .j2 files doesn't matter.

```
d:\GitHub\nw-infrastructure\config-templates\EDGE_MX240\SRX FXP0 TEMPLATES>python prender.py AU1.yml fxp0.j2


#--- start config for AU1 -----------------------------------------------------



--- start config for AU1 CFW ------------------------------------------------------------

delete interfaces fxp0
delete groups node0 interfaces fxp0.0
set groups node0 system backup-router 10.226.32.1
set groups node0 system backup-router destination 10.224.0.0/14
set groups node0 interfaces fxp0 unit 0 family inet address 10.226.32.11/22
set groups node0 interfaces fxp0 unit 0 family inet address 10.226.32.53/22 master-only
set groups node0 routing-options static route 10.224.0.0/14 next-hop 10.226.32.1
...
```

Or you can redirect the output to a file
```
alex.chuvakov@WA1T3NNETHOP01:~/templates$ python prender.py ymx.yml mx.j2 >> AU1.txt
alex.chuvakov@WA1T3NNETHOP01:~/templates$ ls -lh | grep txt
-rw-rw-r-- 1 alex.chuvakov alex.chuvakov 25K Feb 17 21:02 AU1.txt
```
In yaml file you need to define first /24 block form /22 MGMT network assigned to the site.

It can be 10.226.32.116/22 or 10.226.32.0/22 or 10.226.32.116 or 10.226.32.
That doesn't matter since the template takes only first three octets from this network.
