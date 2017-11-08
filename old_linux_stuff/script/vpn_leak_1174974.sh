#!/bin/sh
# Au Nguy

#set -x

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

filename="$host.vpn_leak_check_1174974.log"

cd /var/tmp

time=`date "+%Y-%m-%d %H:%M:%S"`
echo "">> $filename
echo ">>>>>>>>>>>>>>>>>> Start: $time">> $filename

sap_allo=0
sa_key_allo=0
sa_key_allo_fail=0
sa_key_allo_pair_fail=0
sa_key_allo_fail3=0
sa_key_allo_pair_fail3=0
sa_key_pair_allo_fail=0

#1)	From shell as root, execute the commands 3 times a minute apart on all three pics (pic1, pic2, and pic3) on active node (node0 or node1)
#a)	cprod -A node0.fpc5.pic1 -c "show usp ipsec global-stat" | egrep "SA keys|SAP allocated|XLR SAE"
#b)	cprod -A node0.fpc5.pic2 -c "show usp ipsec global-stat" | egrep "SA keys|SAP allocated|XLR SAE"
#c)	cprod -A node0.fpc5.pic3 -c "show usp ipsec global-stat" | egrep "SA keys|SAP allocated|XLR SAE"
#2)	Normally, SA keys allocated should be about twice as SAP allocated.   If the SA keys allocated is 3 times or more, please schedule a failover
#a)	        SAP allocated                       : 971
#b)	        SA keys allocated                   : 1946
#3)	If one of these two fields incrementing between 1st and 3rd run,  please schedule a failover
#a)	        SA key alloc fail                   : 0
#b)	        SA key pair alloc fail              : 0
#4)	If SA key pair allocated over 1000, please schedule a failover
#a)	        SA key pair allocated               : 100
#
#cprod -A node0.fpc5.pic1 -c "show usp ipsec global-stat" | egrep "SA keys|SAP allocated|XLR SAE"
#        XLR SAE context fill fail           : 0
#        XLR SAE add control fail            : 0
#        SAP allocated                       : 971
#        SA keys allocated                   : 1946
#        SA key pair allocated               : 2
#        SA key alloc fail                   : 0
#        SA key pair alloc fail              : 0

if [ "$model" = "srx5600" ];
then
   fpc="fpc5"
   pics="
   $node.$fpc.pic1
   $node.$fpc.pic2
   $node.$fpc.pic3
   "
else
   fpc="fpc1"
   pics="
   $node.$fpc.pic0
   "
fi

tmp_file1="/tmp/1174974_1"
tmp_file2="/tmp/1174974_2"
exit_code=0

for pic in $pics; do
    for n in 1 2 3; do
       echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
       echo ">> show usp ipsec global-stat" | egrep "SA key|SAP allocated|XLR SAE">> $filename
       if [ $n -eq 1 ];
        then
            cprod -A $pic -c "show usp ipsec global-stat" | egrep "SA key|SAP allocated|XLR SAE"> $tmp_file1
            cat $tmp_file1>> $filename
            sa_key_allo_fail=`cat $tmp_file1 | grep "SA key alloc fail"| awk '{print $6}'`
            sa_key_allo_pair_fail=`cat $tmp_file1 | grep "SA key pair alloc fail"| awk '{print $7}'`
        elif [ $n -eq 3 ];
        then
            cprod -A $pic -c "show usp ipsec global-stat" | egrep "SA key|SAP allocated|XLR SAE"> $tmp_file2
            cat $tmp_file2>> $filename
            cat $tmp_file2
            sap_allo=`cat $tmp_file2 | grep "SAP allocated"| awk '{print $4}'`
            sa_key_allo=`cat $tmp_file2 | grep "SA keys allocated"| awk '{print $5}'`
            sa_key_allo_fail2=`cat $tmp_file2 | grep "SA key alloc fail"| awk '{print $6}'`
            sa_key_allo_pair_fail2=`cat $tmp_file2 | grep "SA key pair alloc fail"| awk '{print $7}'`
            sa_key_pair_allo=`cat $tmp_file2 | grep "SA key pair allocated"| awk '{print $6}'`
            
            if [ $sa_key_pair_allo -gt 1000 ]; then
               echo "Failed: SA key pair allocated value $sa_key_pair_allo on $pic met condition for failover or key management restart"
               echo "Failed: SA key pair allocated value $sa_key_pair_allo on $pic met condition for failover or key management restart">> $filename
               exit_code=1
            fi
            
            val=`expr $sa_key_allo / $sap_allo`
            if [ $val -ge 3 ]; then
               echo "Failed: SA key allocated ($sa_key_allo) and SAP allocated ($sap_allo) ratio is 3 or greater on $pic met condition for failover or key management restart"
               echo "Failed: SA key allocated ($sa_key_allo) and SAP allocated ($sap_allo) ratio is 3 or greater on $pic met condition for failover or key management restart">> $filename
               exit_code=1
            fi
            
            if [ $sa_key_allo_fail3 -gt $sa_key_allo_fail ]; then
               echo "Failed: SA key allocated fail incrementing from $sa_key_allo_fail to $sa_key_allo_fail3 on $pic met condition for failover or key management restart"
               echo "Failed: SA key allocated fail incrementing from $sa_key_allo_fail to $sa_key_allo_fail3 on $pic met condition for failover or key management restart">> $filename
               exit_code=1
            fi
        else
            cprod -A $pic -c "show usp ipsec global-stat" | egrep "SA key|SAP allocated|XLR SAE">> $filename
        fi
        
        sleep 10
    done
done

rm $tmp_file1
rm $tmp_file2

if [ $exit_code -eq 1 ];
then
    echo ""
    echo "Router $host $node is a candidate for failover to secondary or"
    echo "Restart IPsec key management via restart ipsec-key-management gracefully"
    echo "Please review the latest data in /var/tmp/$filename for further confirmation"
    echo "Router $host $node is a candidate for failover to secondary or">>$filename
    echo "Restart IPsec key management via restart ipsec-key-management gracefully">> $filename
    echo "Please review the latest data in /var/tmp/$filename for further confirmation">> $filename
    time=`date "+%Y-%m-%d %H:%M:%S"`
    echo ">>>>>>>>>>>>>>>>>> Stop: $time">> $filename
    exit 1
else
    echo ""
    echo "Router $host $node is not affected by VPN leaks PR 1174974 and failover is not necessary"
    echo "Please review the latest data in /var/tmp/$filename for further confirmation"
    echo "Router $host $node is not affected by VPN leaks PR 1174974 and failover is not necessary">> $filename
    echo "Please review the latest data in /var/tmp/$filename for further confirmation">> $filename
    time=`date "+%Y-%m-%d %H:%M:%S"`
    echo ">>>>>>>>>>>>>>>>>> Stop: $time">> $filename
    exit 0
fi
