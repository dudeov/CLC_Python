#!/bin/sh
# Au Nguy

cli -c "show version node local" >/tmp/version
#root@CA1SRX5600-B> show version node local 
#node1:
#--------------------------------------------------------------------------
#Hostname: CA1SRX5600-B
#Model: srx5600
#JUNOS Software Release [12.1X47-D25.4]

model=`cat /tmp/version | grep Model|awk '{print $2}'`
node=`cat /tmp/version | grep node| awk -F: '{print $1}'`
host=`cat /tmp/version | grep Hostname| awk '{print $2}'`

cd /var/script

if [ "$node" = "node0" ];
then
   node="node1"
else
   node="node0"
fi

scripts=`ls *.sh`
for script in $scripts; do
    rcp -T $script $node:/var/script
done