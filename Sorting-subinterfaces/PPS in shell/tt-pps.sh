filename=$1
echo 
echo 'Top 10 pps talkers:'
echo
cat /var/tmp/$filename | grep 'Logical \|Input :' | awk '!(NR%2){print$0p}{p=$0}' | awk -F " " '{print "Interface:",$9,"\tInput pps:",$4}' | awk ' $5 > 1 ' | sort -k 5nr | grep -m10 Input
echo
