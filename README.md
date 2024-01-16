## Start

Start project
```bash
django-admin startproject pretest
```


Collect statistic
```bash
python manage.py collectstatic
```

Runserver
```bash
python manage.py runserver
```

#### Project structure:
```
.
├── README.md
├── accounts
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── aws_deployment.MD
├── contacts
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── digital_ocean_deployment.MD
├── docs.MD
├── listings
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── choices.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_listing_table.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── pages
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── postgresql
│   ├── docker-compose.yml
│   ├── init.sql
│   └── postgresql.conf
├── project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── realtors
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_realtor_table.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── requirements.txt
└── templates
    ├── accounts
    │   ├── dashboard.html
    │   ├── login.html
    │   └── register.html
    ├── admin
    │   └── base_site.html
    ├── base.html
    ├── listings
    │   ├── listing.html
    │   ├── listings.html
    │   └── search.html
    ├── pages
    │   ├── about.html
    │   └── index.html
    └── partials
        ├── _alerts.html
        ├── _footer.html
        ├── _navbar.html
        └── _topbar.html

19 directories, 73 files
```
