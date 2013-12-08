# Raspberry Status
A basement status server for the Raspberry Pi


## Circuit Diagram

TODO


## API Setup

Install virtualenv, and populate dependencies from the requirements.txt file.

Follow the Flask deploy instructions.  For example, [for Apache](http://flask.pocoo.org/docs/deploying/mod_wsgi/):

```apache
<VirtualHost *:80>
    ServerName rsp.example.com
    ServerAlias rsp

    WSGIScriptAlias /api/v1 /path/to/project/apache_wsgi.py
    AliasMatch ^/(?!api)(.*)$ /path/to/project/rsp_status/static/$1

    <Directory "/path/to/project/">
        Options All
        AllowOverride All
        Order allow,deny
        Allow from all
    </Directory>
</VirtualHost>
```


## Sensor Station Setup & Installation

From a fresh raspbian installation.

Add required python packages:

- Install setuptools: `wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | sudo python`
- Install pip: `wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py -O - | sudo python`
- Install requests: `sudo pip install requests`


Clone the repository and add local settings:

- Clone rsp_status: `git clone https://github.com/gthole/rsp_status/`
- Populate a config/settings_local.py file


Set the sensor readings scripts to go at startup:

- Install foreman: `sudo gem install foreman`
- Add init.d script (example below)
- `chmod 755 /etc/init.d/sensors`
- Register `sensors` in update-rc.d


### init.d screen

As simple as possible:

```bash
#! /bin/sh
# /etc/init.d/sensors
#

case "$1" in
  start)
    echo "Starting sensors"
    cd /home/pi/rsp_status/
    /usr/local/bin/foreman start > sensors.log
    ;;
  stop)
    echo "Stopping sensors"
    killall python  # Brutal, but effective.
    ;;
  *)
    echo "Usage: /etc/init.d/sensors {start|stop}"
    exit 1
    ;;
esac

exit 0
```
