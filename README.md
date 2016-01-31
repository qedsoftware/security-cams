Security-cams
==
Some scripts for managing and post-processing the recordings from security cams.

Sharx
==
SHARX cameras have lifecycle policies available for data stored on SD cards.
However, lifecycle management is also needed for the DropBox or FTP servers that these cameras back up their data to, or else disk space exhaustion will quickly occur. 
In the sharx folder,

    data_mgmt.py 

contains a short python script that will do the trick, parsing the filenames and deleting any videos or imagery that are more than MAX_DAYS days old. 
On a Mac or UNIX machine, you can take the following steps to automate the execution of the script on a daily basis:

    1. chmod ugo+x data_mgmt.py
    2. place a copy of the file inside the DropBox folder (Dropbox/Apps/Sharx)
    3. edit crontab (crontab -e) with the following line:

    @daily cd /path/to/data/Sharx && ./data_mgmt.py >> sharx.log

    where sharx.log is a logfile.
