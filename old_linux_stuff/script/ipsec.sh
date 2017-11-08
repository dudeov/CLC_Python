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

cd /var/tmp

filename=`date "+%Y-%m-%d-%H-%M-%S.$host.$node.eng_data_ipsec.log"`

time=`date "+%Y-%m-%d %H:%M:%S"`
echo ">> Start: $time">> $filename

if [ $# -lt 1 ]; then
    echo
    echo usage -
    echo " first parameter is vpn tunnel name (required)"
    exit
fi

vpn=$1

if [ "$model" = "srx5600" ];
then
   fpc="fpc5"
   pics="
   node0.$fpc.pic0
   node0.$fpc.pic1
   node0.$fpc.pic2
   node0.$fpc.pic3
   node1.$fpc.pic0
   node1.$fpc.pic1
   node1.$fpc.pic2
   node1.$fpc.pic3
   "
else
   fpc="fpc1"
   pics="
   node0.$fpc.pic0
   node1.$fpc.pic0
   "
fi

# cli commands
echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> show security ike security-associations | no-more">> $filename
cli -c "show security ike security-associations | no-more" >> $filename

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> show security ipsec security-associations | no-more">> $filename
cli -c "show security ipsec security-associations | no-more" >> $filename

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> show security ipsec security-associations vpn-name $vpn detail">> $filename
cli -c "show security ipsec security-associations vpn-name $vpn detail" >> $filename

# get all the sa indexes from vpn-name
#root@WA1-SRX-CORE-N1> show security ipsec security-associations vpn-name au1-vpn detail | grep ID: 
#  ID: 909 Virtual-system: root, VPN Name: au1-vpn
#  ID: 2517 Virtual-system: root, VPN Name: au1-vpn
#  ID: 2617 Virtual-system: root, VPN Name: au1-vpn
all_sa=`cli -c "show security ipsec security-associations vpn-name $vpn detail| grep ID: "| awk '{print $2}'`

# abort if no sa index found
if [ -z "$all_sa" ]; then
   echo "No SA index found for VPN tunnel $vpn.  Check if VPN name is valid"
   echo "No SA index found for VPN tunnel $vpn.  Check if VPN name is valid">> $filename
   echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
   echo ">> show security ipsec security-associations vpn-name $vpn detail">> $filename
   cli -c "show security ipsec security-associations vpn-name $vpn detail" >> $filename
   exit
fi

for sa in $all_sa; do
    echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
    echo ">> show security ipsec security-associations index $sa detail | no-more">> $filename
    cli -c "show security ipsec security-associations index $sa detail | no-more" >> $filename
done


echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> show security ipsec statistics">> $filename
cli -c "show security ipsec statistics | no-more" >> $filename

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> show security flow session summary">> $filename
cli -c "show security flow session summary | no-more" >> $filename

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> show security monitoring performance spu">> $filename
cli -c "show security monitoring performance spu | no-more" >> $filename

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> show security flow statistics">> $filename
cli -c "show security flow statistics | no-more" >> $filename

for n in 1 2 3; do
        echo ">> Iteration: $n" >> $filename
	for pic in $pics; do
               for sa in $all_sa; do
                    echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
                    echo ">> show usp ipsec sa $sa">> $filename
	            cprod -A $pic -c "show usp ipsec sa $sa" >> $filename
               done

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> show usp ipsec cp global-stat">> $filename
	       cprod -A $pic -c "show usp ipsec cp global-stat" >> $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> show usp ipsec dist-table">> $filename
	       cprod -A $pic -c "show usp ipsec dist-table" >> $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> show usp ipsec cp global-stat">> $filename
	       cprod -A $pic -c "show usp ipsec cp global-stat" >> $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> show usp flow stats">> $filename
	       cprod -A $pic -c "show usp flow stats" >> $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> show usp flow counters all">> $filename
	       cprod -A $pic -c "show usp flow counters all" >> $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> show usp ipsec stats">> $filename
	       cprod -A $pic -c "show usp ipsec stat" >> $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> show usp ipsec global-stat">> $filename
               cprod -A $pic -c "show usp ipsec global-stat" >> $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> show usp ipsec pkt-stat">> $filename
               cprod -A $pic -c "show usp ipsec pkt-stat" >> $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> show usp ipsec mini-sa">> $filename
               cprod -A $pic -c "show usp ipsec mini-sa" >> $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> show usp ipsec mini-sa-stats">> $filename
               cprod -A $pic -c "show usp ipsec mini-sa-stats" >> $filename

               #echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               #echo ">> show usp flow session tunnel">> $filename
               #cprod -A $pic -c "show usp flow session tunnel" >> $filename
          done
  sleep 10
done

time=`date "+%Y-%m-%d %H:%M:%S"`
echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> Stop: $time">> $filename

tar -czf $filename.tgz $filename

if [ -f $filename.tgz ]; then
	rm $filename
        echo "Done!!!"
        echo "From /var/tmp, sftp to anonymous@sftp.juniper.net using password anonymous"
        echo "Create a directory, mkdir pub/incoming/2016-0614-0075"
        echo "Copy the file there, put $filename.tgz"
fi
