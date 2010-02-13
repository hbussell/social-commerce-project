=======================
social-commerce-project
=======================

Sample project to help you get started using Pinax and Satchmo to create great
social e-commerce websites.

The current version uses Django 1.1.1, Pinax 0.7.1 and Satchmo trunk.

This has been tested with python 2.5 and 2.6

Check out a sample site here.
http://social-commerce-demo.hbussell.com
You can login with demo:demo


------------
Installation
------------

Create the virutalenv ::

    mkdir test-site
    virtualenv --no-site-packages env
    source env/bin/activate
    easy_install pip

Get the social-commerce-project ::    

    git clone git://github.com/hbussell/social-commerce-project.git

Install the requirements ::
    cd social-commerce-project/socialcommerce
    pip install -r requirements.txt

    # or you can use stable-requirements.txt to install specific editable
    versions

Create the database and optionally load the sample data ::    
    python manage.py syncdb
    python manage.py satchmo_load_l10n
    python manage.py satchmo_load_store

If you are using MySQL satchmo requires utf-8 ::

    DATABASE_OPTIONS = {
       'init_command' : 'SET NAMES "utf8"',
       }


Find out more options for the satchmo configuration 
http://www.satchmoproject.com/docs/svn/new_installation.html#customizing-the-settings

Start it up ::
    python manage.py runserver
