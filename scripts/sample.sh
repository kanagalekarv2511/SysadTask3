#!/bin/bash 
echo -e " ================Uptime is =====================\n" >> /tmp/complog.txt
uptime >> /tmp/complog.txt
echo -e " ================Disk or Filesystem usage is =====================\n" >> /tmp/complog.txt
df -m  >> /tmp/complog.txt
echo -e " ================Memory  usage is =====================\n" >> /tmp/complog.txt
free -m   >> /tmp/complog.txt
echo -e " ================Utilization and Most expensive processes  =====================\n" >> /tmp/complog.txt
top -b -n 1   >> /tmp/complog.txt
echo -e " ================Current Connections  =====================\n" >> /tmp/complog.txt
who   >> /tmp/complog.txt
echo -e " ================List of Process  =====================\n" >> /tmp/complog.txt
ps -ef    >> /tmp/complog.txt

