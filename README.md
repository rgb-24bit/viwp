# Deploy viwp on nginx server

> This is a summary of my experience in trying to deploy viwp to the nginx server.

## uWSGI

First, download uwsgi to the virtual environment:

```
$ pipenv install uwsgi
```

Then edit the uwsgi configuration file [uwsgi_conf.ini](conf/uwsgi_conf.ini).

Run the command `pipenv run uwsgi uwsgi_conf.ini` to check whether the configuration is successful.

## Supervisor

Install Supervisor through the system's package management tool or pip:

```
$ apt-get install supervisor
```

Modify the configuration file [viwp.conf](conf/viwp.conf) and copy it to the directory `/etc/supervisor/conf.d/`.

Then restart the supervisor service:

```
$ service supervisor restart 
```

## Nginx

Install nginx and replace the contents of `/etc/nginx/sites-available/default` with the content in use [nginx.conf](conf/nginx.conf).

## Problem

These are the problem domain solutions I encountered during the deployment process.

+ uWSGI compilation failed

```
$ apt-get install python3-all-dev
```

+ Supervisor required socket file is missing, making it unable to start

```
$ python -c "import socket as s; sock = s.socket(s.AF_UNIX); sock.bind('/var/run/supervisor.sock')"
```

## Reference

+ [Configuring uWSGI — uWSGI 2.0 documentation](https://uwsgi-docs.readthedocs.io/en/latest/Configuration.html)
+ [Nginx support — uWSGI 2.0 documentation](https://uwsgi-docs.readthedocs.io/en/latest/Nginx.html)
+ [Configuration File — Supervisor 3.3.5 documentation](http://supervisord.org/configuration.html)

