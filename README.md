## Start
Star the project
```bash
django-admin startproject project . 
```

Create app pages
```bash
python manage.py startapp pages
```

Run the server
```bash
python manage.py runserver 
```

Run the server
```bash
python manage.py runserver 
```

Collect static
```bash
python manage.py collectstatic
```

```
.
├── README.md
├── app_requirement.MD
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
    ├── admin
    │   └── base_site.html
    ├── base.html
    ├── listings
    │   ├── listing.html
    │   ├── listings.html
    │   └── search.html
    └── pages
        ├── about.html
        └── index.html

13 directories, 48 files
```
