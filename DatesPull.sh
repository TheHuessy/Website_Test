#!/bin/bash
#!/bin/bash
#!/usr/bin/python3
#!/usr/bin/git


DATE=$(date +"%m%d%Y")

cd /home/pi/Documents/Website_Test
echo $DATE > /home/pi/Documents/Website_Test/ETL.log 2>&1
sudo /usr/bin/python DatesPull.py >> /home/pi/Documents/Website_Test/ETL.log 2>&1
echo --------------------- >> /home/pi/Documents/Website_Test/ETL.log 2>&1
echo PULLING... >> /home/pi/Documents/Website_Test/ETL.log 2>&1
sudo /usr/bin/git pull >> /home/pi/Documents/Website_Test/ETL.log 2>&1
echo ADDING... >> /home/pi/Documents/Website_Test/ETL.log 2>&1
sudo /usr/bin/git add . >> /home/pi/Documents/Website_Test/ETL.log 2>&1
echo COMMITTING... >> /home/pi/Documents/Website_Test/ETL.log 2>&1
sudo /usr/bin/git commit -m 'auto_commit_$DATE' >> /home/pi/Documents/Website_Test/ETL.log 2>&1
echo PUSHING >> /home/pi/Documents/Website_Test/ETL.log 2>&1
echo /usr/bin/git config --global user.name >> /home/pi/Documents/Website_Test/ETL.log 2>&1
sudo /usr/bin/git push origin master >> /home/pi/Documents/Website_Test/ETL.log 2>&1
echo ===================== >> /home/pi/Documents/Website_Test/ETL.log 2>&1
