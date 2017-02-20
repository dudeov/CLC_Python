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

filename="$host.disable_pause_1192536.log"

cd /var/tmp

time=`date "+%Y-%m-%d %H:%M:%S"`
echo "">> $filename
echo ">>>>>>>>>>>>>>>>>> Start: $time">> $filename

if [ "$model" = "srx5600" ];
then
   fpc="fpc1"
   pics="
   node0.$fpc
   node1.$fpc
   "
else
   echo "$model is not affected by PR1192536.  No changes are needed.";
   exit
fi

# write to register
for pic in $pics; do
       echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
       echo ">> bringup jspec write mdmt_0 register HG 0 core CFG PAUSE_ENA 0">> $filename
       cprod -A $pic -c "bringup jspec write mdmt_0 register HG 0 core CFG PAUSE_ENA 0" >> $filename

       echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
       echo ">> bringup jspec write mdmt_0 register HG 1 core CFG PAUSE_ENA 0 ">> $filename
       cprod -A $pic -c "bringup jspec write mdmt_0 register HG 1 core CFG PAUSE_ENA 0" >> $filename

       echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
       echo ">> bringup jspec write mdmt_1 register HG 0 core CFG PAUSE_ENA 0">> $filename
       cprod -A $pic -c "bringup jspec write mdmt_1 register HG 0 core CFG PAUSE_ENA 0" >> $filename

       echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
       echo ">> bringup jspec write mdmt_1 register HG 1 core CFG PAUSE_ENA 0">> $filename
       cprod -A $pic -c "bringup jspec write mdmt_1 register HG 1 core CFG PAUSE_ENA 0" >> $filename
done

#FIOC0(applebert vty)# bringup jspec read mdmt_0 register HG 0 core CFG    
#0x404  MiddleMount.HG[0].core.CFG         00264003   
#                                   PAUSE_ENA[21:21] : 0x1
# ...
tmp_file="/tmp/disable_pause"
exitcode=0
#0 = success
#1 = failure

for pic in $pics; do
    echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
    echo ">> bringup jspec read mdmt_0 register HG 0 core CFG">> $filename
    cprod -A $pic -c "bringup jspec read mdmt_0 register HG 0 core CFG" > $tmp_file
    cat $tmp_file>> $filename    
    reg=`cat $tmp_file| grep PAUSE_ENA|awk '{print $3}'`
    if [ $reg = "0x0" ]; then
    else
        echo "Failed:  Disable pause frame on mdmt 0 HG 0 was not successful on $host $node"
        echo "Failed:  Disable pause frame on mdmt 0 HG 0 was not successful on $host $node">>$filename
        exitcode=1
    fi

    echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
    echo ">> bringup jspec read mdmt_0 register HG 1 core CFG  ">> $filename
    cprod -A $pic -c "bringup jspec read mdmt_0 register HG 1 core CFG" > $tmp_file
    cat $tmp_file>> $filename
    reg=`cat $tmp_file| grep PAUSE_ENA|awk '{print $3}'`
    if [ $reg = "0x0" ]; then
    else
        echo "Failed:  Disable pause frame on mdmt 0 HG 1 was not successful on $host $node"
        echo "Failed:  Disable pause frame on mdmt 0 HG 1 was not successful on $host $node">>$filename
        exitcode=1
    fi

    echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
    echo ">> bringup jspec read mdmt_1 register HG 0 core CFG ">> $filename
    cprod -A $pic -c "bringup jspec read mdmt_1 register HG 0 core CFG" > $tmp_file
    cat $tmp_file>> $filename
    reg=`cat $tmp_file| grep PAUSE_ENA|awk '{print $3}'`
    if [ $reg = "0x0" ]; then
    else
        echo "Failed:  Disable pause frame on mdmt 1 HG 0 was not successful on $host $node"
        echo "Failed:  Disable pause frame on mdmt 1 HG 0 was not successful on $host $node">>$filename
        exitcode=1
    fi

    echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
    echo ">> bringup jspec read mdmt_1 register HG 1 core CFG ">> $filename
    cprod -A $pic -c "bringup jspec read mdmt_1 register HG 1 core CFG" > $tmp_file
    cat $tmp_file>> $filename
    reg=`cat $tmp_file| grep PAUSE_ENA|awk '{print $3}'`
    if [ $reg = "0x0" ]; then
    else
        echo "Failed:  Disable pause frame on mdmt 1 HG 1 was not successful on $host $node"
        echo "Failed:  Disable pause frame on mdmt 1 HG 1 was not successful on $host $node">>$filename
        exitcode=1
    fi

done

rm $tmp_file

if [ $exitcode -eq 1 ];
then
    time=`date "+%Y-%m-%d %H:%M:%S"`
    echo ">>>>>>>>>>>>>>>>>> Stop: $time">> $filename
    exit 1
else
    echo "Workaround for PR1192536 has been programmed successfully on $host $node"
    echo "Workaround for PR1192536 has been programmed successfully on $host $node">> $filename
    echo "Run the script again if one of the nodes is cluster has been rebooted"
    echo "Run the script again if one of the nodes is cluster has been rebooted">> $filename
    time=`date "+%Y-%m-%d %H:%M:%S"`
    echo ">>>>>>>>>>>>>>>>>> Stop: $time">> $filename
    exit 0
fi