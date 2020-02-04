#!/bin/bash
#!/bin/bash
#!/usr/bin/python3
#!/usr/bin/git


DATE_T=$(date +"%m%d%Y")
cd /home/pi/Documents/Website_Test
sudo echo "$DATE_T" > /home/pi/Documents/Website_Test/ETL.log 2>&1

# ls >> /home/pi/Documents/Website_Test/ETL.log 2>&1
echo $DATE_T > /home/pi/Documents/Website_Test/ETL.log 2>&1
# sudo /usr/bin/python3 DatesPull.py >> /home/pi/Documents/Website_Test/ETL.log 2>&1
echo --------------------- >> /home/pi/Documents/Website_Test/ETL.log 2>&1
echo PULLING... >> /home/pi/Documents/Website_Test/ETL.log 2>&1
# sudo -l /usr/bin/git pull >> /home/pi/Documents/Website_Test/ETL.log 2>&1


/bin/bash -c "git status" >> /home/pi/Documents/Website_Test/ETL.log 2>&1
su -s /bin/bash pi -c "git pull" >> /home/pi/Documents/Website_Test/ETL.log 2>&1
echo ADDING... >> /home/pi/Documents/Website_Test/ETL.log 2>&1
su -s /bin/bash pi -c "git add -A"
echo CONFIGGING... >> /home/pi/Documents/Website_Test/ETL.log 2>&1
su -s /bin/bash pi -c "git config --global user.email jameshuessy@gmail.com " >> /home/pi/Documents/Website_Test/ETL.log 2>&1
su -s /bin/bash pi -c "git config --global user.name TheHuessy " >> /home/pi/Documents/Website_Test/ETL.log 2>&1

echo COMMITTING... >> /home/pi/Documents/Website_Test/ETL.log 2>&1
su -s /bin/bash pi -c "git commit -m 'auto_commit_${DATE_T}'" >> /home/pi/Documents/Website_Test/ETL.log 2>&1
echo PUSHING >> /home/pi/Documents/Website_Test/ETL.log 2>&1
su -s /bin/bash pi -c "git push"
# sudo /usr/bin/git push origin master >> /home/pi/Documents/Website_Test/ETL.log 2>&1
echo ===================== >> /home/pi/Documents/Website_Test/ETL.log 2>&1
