# DIGITAL OCEAN DJANGO DEPLOYMENT

Reference: [Django Deployment to Ubuntu 18.04](https://gist.github.com/bradtraversy/cfa565b879ff1458dba08f423cb01d71)

## Set up droplet Ubuntu server

SSH key generator
```bash
ls ./.ssh
ssh-keygen
Enter file in which to save the key (/Users/kato/.ssh/id_rsa): /Users/kato/.ssh/id_rsa_dj
```

Copy SSH key into Digital Ocean
```bash
cat ./.ssh/id_rsa_dj.pub
```

Add identity
```bash
ssh-add ./.ssh/id_rsa_dj
```

Access Server
```bash
ssh root@128.199.108.7
```

### Create a new user
It will ask for a password, use something secure. You can just hit enter through all the fields. I used the user "djangoadmin" but you can use anything

```
# adduser djangoadmin
pw. 123456
```

Give root privileges
```
# usermod -aG sudo djangoadmin
```

Access server with new user
```bash
ssh djangoadmin@128.199.108.7
-> Deny, need to create SSH keys for the new user
```

SSH keys for the new user
```bash
# After login as root
cd ..
cd home/djangoadmin
ls -a
```
Now we need to setup SSH keys for the new user. You will need to get them from your local machine
```bash
mkdir .ssh
cd .ssh
nano authorized_keys
```

Open the new tab and get the key from id_rsa-dj.pub
```
# Copy rsa key to authorized_keys
cat ./.ssh/id_rsa_dj.pub
```
After that, we can access Ubuntu server by `ssh djangoadmin@128.199.108.7`

### Disable root login
Set PermitRootLogin to no and restart the server
```bash
sudo nano /etc/ssh/sshd_config

# After change PermitRootLogin to no
sudo systemctl reload sshd
```

### Simple Firewall Setup

See which apps are registered with the firewall
```bash
sudo ufw app list

# Available applications:
# OpenSSH
sudo ufw allow OpenSSH
sudo ufw enable

# To see the firewall status
sudo ufw status 
```
## Software Installation
Update packages
```bash
sudo apt update
sudo apt upgrade
```
Install python3, postgres & Nginx
```bash
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl
```

### Set up PostgreSQL database & user

```markdown
sudo -u postgres psql

# SQL syntax
CREATE DATABASE django;
CREATE USER dbadmin WITH PASSWORD '123456@pw';
ALTER ROLE dbadmin SET client_encoding TO 'utf8';
ALTER ROLE dbadmin SET default_transaction_isolation TO 'read committed';
ALTER ROLE dbadmin SET timezone to 'UTC';
GRANT ALL PRIVILEGES ON DATABASE django TO dbadmin;
```
### Set up Virtual Env
Install package
```markdown
sudo apt install python3-venv
```

Set up virtual env
```bash
cd
mkdir pyapps
cd pyapps
python3 -m venv ./venv

# active virtual env
source venv/bin/activate
```

## Git & Upload

Install dependencies on project and add to git
```bash
pip freeze > requirements.txt
```

Generate access token for a repo:
> Setting / Personal access tokens / Tokens (classic)

Clone project into the app folder on the server [Either HTTPs or setup SSH keys]
```
git clone https://[auth2:TOKEN]@github.com/Katoo2706/django_project.git
```

Install pip modules from requirements
```bash
pip install --no-cache-dir --ignore-installed -r django_project/requirements.txt
```
## Local Settings Setup

Add code to your settings.py file and push to server
```python
try:
    from .local_settings import *
except ImportError:
    pass
```

Or using python decouple

After pull the latest code, make migrations and collect statistic
```bash
python manage.py makemigrations
python manage.py migrate
```

Create superuser
```bash
python manage.py createsuperuser
```

Collect static
```bash
python manage.py collectstatic
```

Create exception for port 8000
```bash
sudo ufw allow 8000
```

Run the server
```bash
python manage.py runserver 0.0.0.0:8000
```