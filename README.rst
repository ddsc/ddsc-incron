ddsc-incron
===========

One of the options to import data within DDSC is via SFTP. Once a new file has been uploaded, it needs to be processed and stored immediately. The inotify cron system is used to watch directories and run Python code (see `notify.py <https://github.com/ddsc/ddsc-incron/blob/master/ddsc_incron/notify.py>`_) after every new file upload.