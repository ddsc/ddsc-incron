ddsc-incron
===========

One of the ways to import data within DDSC is via SFTP. Once a new file has been uploaded, it needs to be processed and stored immediately. The inotify cron system is used to watch directories and run Python code (see `notify.py <https://github.com/ddsc/ddsc-incron/blob/master/ddsc_incron/notify.py>`_) after every file upload.

Building ddsc-incron
--------------------

To build ddsc-incron successfully, Python headers files need to be present. On Ubuntu::

	sudo apt-get install python-dev

If all is well and `git <http://git-scm.com/>`_ is present, ddsc-incron should now build smoothly::

	git clone git@github.com:ddsc/ddsc-incron.git
	cd ddsc-incron
	python bootstrap.py
	bin/buildout