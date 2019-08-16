#usr/bin/bash/

cd /home/james/Documents/JavaScript

## DO A PYTHON CALL FOR THE DAILY UPDATE SCRIPT WHICH YOU HAVE ##
### Maybe also consider pushing it since it doesn't have any sensitive info

#/usr/bin/git status > /home/james/Documents/Cronlog.txt
DATE=`date`
echo $DATE > /home/james/Documents/Cronlog.txt
/usr/bin/git add . >> /home/james/Documents/Cronlog.txt
/usr/bin/git commit -m 'auto-commit' >> /home/james/Documents/Cronlog.txt
/usr/bin/git push >> /home/james/Documents/Cronlog.txt
/usr/bin/git status >> /home/james/Documents/Cronlog.txt
DATE=`date`
echo ================ >> /home/james/Documents/Cronlog.txt
echo $DATE >> /home/james/Documents/Cronlog.txt
echo ================ >> /home/james/Documents/Cronlog.txt


## HOW THIS WORKS ##

# Key things:
	# -When specifying directories, you have to put a '/' in front of the
	# first directory part.
	# -When writing to the log file, a single '>' means overwrite
	# -The double '>>' means append. This script overwrites the file with
	# the first pipe and then appends to it with each pipe line after
		# This script will essentailly rewrite the contents of the
		# log starting with the first 'status' command 




