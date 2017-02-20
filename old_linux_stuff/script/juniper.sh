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

filename=`date "+%Y-%m-%d-%H-%M-%S.$host.$node.eng_data.log"`

cd /var/tmp

time=`date "+%Y-%m-%d %H:%M:%S"`
echo ">> Start: $time">> $filename

# cli commands
echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> show chassis cluster status">> $filename
cli -c "show chassis cluster status | no-more" >> $filename

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> show chassis cluster statistics">> $filename
cli -c "show chassis cluster statistics | no-more" >> $filename

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> show chassis cluster interfaces">> $filename
cli -c "show chassis cluster interfaces | no-more" >> $filename

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> show chassis cluster information">> $filename
cli -c "show chassis cluster information | no-more" >> $filename

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> show chassis fpc">> $filename
cli -c "show chassis fpc | no-more" >> $filename

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> show chassis fpc pic-status">> $filename
cli -c "show chassis fpc pic-status | no-more" >> $filename

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> show pfe terse">> $filename
cli -c "show pfe terse | no-more" >> $filename

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> show chassis routing-engine">> $filename
cli -c "show chassis routing-engine | no-more" >> $filename

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> show krt queue">> $filename
cli -c "show krt queue | no-more" >> $filename

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> show system processes extensive">> $filename
cli -c "show system processes extensive| no-more" >> $filename

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> show task memory">> $filename
cli -c "show task memory | no-more" >> $filename

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> show task memory detail">> $filename
cli -c "show task memory detail | no-more" >> $filename

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
echo ">> show chassis alarms">> $filename
cli -c "show chassis alarms | no-more" >> $filename

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> show security flow statistics">> $filename
cli -c "show security flow statistics | no-more" >> $filename

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> show interfaces terse">> $filename
cli -c "show interfaces terse | match reth | no-more" >> $filename

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> ifsmon -c">> $filename
ifsmon -c >> $filename

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> ifsmon -Pd">> $filename
ifsmon -Pd >> $filename

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> ifsmon -Id">> $filename
ifsmon -Id >> $filename

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

for n in 1 2 3 4 5; do
        echo ">> Iteration: $n" >> $filename
	for pic in $pics; do
               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> show xlr pkt_mbuf">> $filename
	       cprod -A $pic -c "show xlr pkt_mbuf" >> $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> show xlr cpu">> $filename
               cprod -A $pic -c "show xlr cpu" >> $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> test watchdog snapshot">> $filename
               cprod -A $pic -c "test watchdog snapshot" >> $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> show watchdog snapshot">> $filename
               cprod -A $pic -c "show watchdog snapshot" >> $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> show usp flow stats">> $filename
               cprod -A $pic -c "show usp flow stats" >> $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> show usp flow counters all">> $filename
               cprod -A $pic -c "show usp flow counters all" >> $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> show usp flow session summary">> $filename
               cprod -A $pic -c "show usp flow session summary" >> $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> show xlr session detail">> $filename
               cprod -A $pic -c "show xlr session detail" >> $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> show xlr pkt_mbuf timeout">> $filename
               cprod -A $pic -c show xlr pkt_mbuf timeout>>  $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> show xlr pkt_mbuf use">> $filename
               cprod -A $pic -c show xlr pkt_mbuf use>>  $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> show mbuf host">> $filename
               cprod -A $pic -c show mbuf host>>  $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
	       echo ">> show mbuf counter">> $filename
               cprod -A $pic -c show mbuf counter>>  $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> show mbuf timeout">> $filename
               cprod -A $pic -c show mbuf timeout>> $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename  
               echo ">> show arena">> $filename
               cprod -A $pic -c show arena>>  $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
	       echo ">> show services objcache">> $filename
               cprod -A $pic -c show services objcache>>  $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> show arena" >> $filename
               cprod -A $pic -c show arena>>  $filename

               echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
               echo ">> show spu " >> $filename
               cprod -A $pic -c show arena>>  $filename
          done

  sleep 20
done

myfpcs="
node1.$fpc
node0.$fpc
"
for myfpc in $myfpcs; do
    echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
    echo ">> show spu-pic stats">> $filename
    cprod -A $myfpc -c "show spu-pic stats" >> $filename
done

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> ifsmon -c">> $filename
ifsmon -c >> $filename

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> ifsmon -Pd">> $filename
ifsmon -Pd >> $filename

echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> ifsmon -Id">> $filename
ifsmon -Id >> $filename

time=`date "+%Y-%m-%d %H:%M:%S"`
echo `date "+%Y-%m-%d %H:%M:%S"`>> $filename
echo ">> Stop: $time">> $filename

tar -czf $filename.tgz $filename

if [ -f $filename.tgz ]; then
	rm $filename
        echo "Done!!!"
        echo "From /var/tmp, sftp to anonymous@sftp.juniper.net using password anonymous"
        echo "Create a directory, mkdir pub/incoming/2016-0606-0886"
        echo "Copy the file there, put $filename.tgz"
fi
