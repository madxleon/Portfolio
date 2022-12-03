#!/bin/sh
CURL="curl -Is http://www.google.com" 

CURLHTTP="http://www.google.com"
DATE=`date '+%Y-%m-%d %H:%M:%S'`
to=""
from="a92leonov@gmail.com"
email_config="
-S smtp-use-starttls \
-S ssl-verify=ignore \
-S smtp-auth=login \
-S smtp=smtp://smtp.gmail.com:587 \
-S from=$from \
-S smtp-auth-user=username \
-S smtp-auth-password=password \
-S ssl-verify=ignore \
-S nss-config-dir=/etc/pki/nssdb \
$to"

function loop {
x=''
CURL="curl -Is http://www.google.com" 
while :
do
x=$(curl -Is http://www.google.com | head -1 | awk '{print $3}')
if [ -z "$x" ]; then
   echo "$DATE Site unavailable"
else 
    echo "$DATE Site available"
    break
fi
done
}

x=$(curl -Is http://www.google.com | head -1 | awk '{print $3}')
if [ -n "$x" ] ; then
        echo $DATE   Site available
else
                echo "$DATE Site unavailable" 
                mail -s "Check site" $email_config
                loop
fi