# AWS DJANGO APPLICATION DEPLOYMENT

### Create AWS Root account & IAM user (developers role)

### Set up MFA

### Create access key
[Access key](https://us-east-1.console.aws.amazon.com/iamv2/home?region=ap-southeast-2#/users/details/kato/create-access-key)

### Set up AWS Command Line Interface
[Download url](https://aws.amazon.com/cli/)

```bash
aws --version
aws configure
```

Configuration for Sydney
`
AWS Access Key ID [None]: **-- ID --**
AWS Secret Access Key [None]: **-- Key --**
Default region name [None]: ap-southeast-2
Default output format [None]: json
`

## Hosting static files on S3
- Create Bucket
- Allow public access
- Edit policy -> Policy generator (S3 Bucket Policy / * / GetObject / {arn:aws:s3:::djangorealestate}/*)

## Install packages to deploy Python Django
> pip install -U boto3

> pip install -U django-storages

- Add `storages` app in settings.py
```
AWS_ACCESS_KEY_ID = 'AKIATCQNDK5VCF4J4N5I'
AWS_SECRET_ACCESS_KEY = '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'

# S3 configuration setting
AWS_STORAGE_BUCKET_NAME = 'djangorealestate'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_FILE_OVERWRITE = False  # Keep both file with same name
```

## Create AWS RDS (Postgresql engine)
- Engine
- Tier
- Master user
- Database name -> update in settings.py

**Config Security**

```markdown
Security
VPC security groups
Choose the Security Group ID / Inbound rules / Edit inbound rules -> Add 2 inbound rules:
/ Allow all access for IPv4 and IPv6
___________________________
|    Type     |   Source  |
|-------------|-----------|
| All traffic | 0.0.0.0/0 |
| All traffic | ::/0      |
---------------------------
```

## Security tips:
- Before we deploy our project, we must make sure that debug = False
- Store all important information, access key in environment variables

## Elastic Beanstalk
- Take care of all infrastructure, E.g: EC2 instances, Elastic Load Balancer, Auto Scaling Group, RDS,..
- Allows the developer to only focus on deploy the application

> Amazon Elastic Beanstalk:
> [Amazon Elastic Beanstalk - Pricing](https://aws.amazon.com/elasticbeanstalk/pricing/)

> Application Load Balancer:
> [Application Load Balancer - Pricing](https://aws.amazon.com/elasticloadbalancing/pricing/)

Install aws eb client (eb) - MacOS
```bash
brew install awsebcli
```

### Utilising AWS Elastic Beanstalk - [Important]
AWS Elastic Beanstalk is very sensitive to certain packages, so for clarify we will run a pre-test to understand it's infrastructure better before deployment

1. Start project. Deploy pretest project
```bash
# folder dev
python3 -m venv ./venv
pip install django
pip install gunicorn
django-admin startproject pretest
```
2. Create project/.ebextensions/django.config
```markdown
option_settings:
 aws:elasticbeanstalk:container:python:
  WSGIPath: pretest.wsgi:application
```
> WSGIPath == < WSGI_APPLICATION = 'pretest.wsgi.application' > (settings.py)

Create requirements.txt
```bash
pip freeze > requirements.txt
```
3. Config aws & eb
```bash
aws configure
```

Using `.ebignore` to ignore file when deployment

Deploy Elastic Bean `eb init`
```markdown
# Configuration
Select a default rxegion: 8
Enter Application Name (default is "pretest"): dev
Python version: 1. Python 3.11 running on 64bit Amazon Linux 2023
Do you want to set up SSH for your instances? n
```
Create EB instance `eb create`
```markdown
Enter Environment Name (default is dev-pretest):
Enter DNS CNAME prefix (default is dev-pretest):
Select a load balancer type: 2
Would you like to enable Spot Fleet requests for this environment? (y/N): N
Type "view" to see the policy, or just press ENTER to continue:
```