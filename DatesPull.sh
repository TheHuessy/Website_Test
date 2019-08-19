#!/bin/bash
#!/bin/bash
#!/usr/bin/python3
#!/usr/bin/git


DATE = `date`

cd /home/pi/Documents/Website_Test
/usr/bin/python3 DatesPull.py > /home/pi/Documents/Website_Test/ETL.log 2>&1
echo --------------------- >> /home/pi/Documents/Website_Test/ETL.log 2>&1
/usr/bin/git add . >> /home/pi/Documents/Website_Test/ETL.log 2>&1
/usr/bin/git commit -m 'auto_commit_$DATE' >> /home/pi/Documents/Website_Test/ETL.log 2>&1
/usr/bin/git push >> /home/pi/Documents/Website_Test/ETL.log 2>&1
echo ===================== >> /home/pi/Documents/Website_Test/ETL.log 2>&1
