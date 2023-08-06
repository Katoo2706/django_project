## Django.contrib

Trong Django, `django.contrib` là một module chứa các ứng dụng tích hợp sẵn cung cấp các chức năng hữu ích để phát triển ứng dụng web một cách nhanh chóng. Các ứng dụng trong `django.contrib` được gọi là "các ứng dụng tích hợp" (built-in apps) và cung cấp các tính năng phổ biến và tiện ích mà bạn có thể sử dụng trong dự án Django của mình.

Dưới đây là một số ứng dụng quan trọng trong `django.contrib`:

- `django.contrib.admin`: Trang quản trị Django.
- `django.contrib.auth`: Hệ thống xác thực và quản lý người dùng.
- `django.contrib.sessions`: Quản lý phiên làm việc của người dùng.
- `django.contrib.messages`: Cơ chế thông báo cho người dùng.
- `django.contrib.staticfiles`: Quản lý và phục vụ tệp tĩnh.
- `django.contrib.contenttypes`: Quản lý kiểu đối tượng và quan hệ giữa các đối tượng.

### Cấu trúc dự án Django

- **app**: Thư mục chứa ứng dụng "app", bao gồm các file và thư mục sau:
  - **admin.py**: Cấu hình trang quản trị Django.
  - **apps.py**: Cấu hình ứng dụng "pages".
  - **migrations**: Chứa các file migration để thay đổi cấu trúc cơ sở dữ liệu.
  - **models.py**: Chứa các model của ứng dụng, bao gồm Data model
  - **tests.py**: Chứa các test cho ứng dụng.
  - **urls.py**: Định tuyến URL cho ứng dụng.
  - **views.py**: Chứa các view của ứng dụng.

- **project**: Thư mục chứa cấu hình chung cho dự án Django, bao gồm các file sau:
  - **manage.py**: Quản lý dự án Django, chạy server, tạo cơ sở dữ liệu, chạy các lệnh tạo migration và nhiều tác vụ quản lý dự án khác.
  - **asgi.py**: Cấu hình ASGI (Asynchronous Server Gateway Interface) cho ứng dụng.
  - **settings.py**: Cấu hình chung cho dự án Django.
  - **urls.py**: Định tuyến URL chung cho dự án.
  - **wsgi.py**: Cấu hình WSGI (Web Server Gateway Interface) cho ứng dụng.

### Database usage
In this project, I config MongoDB as default databbae
```
Requirements: 
- djongo
- pytz # fix can not use djngo
- pymongo==3.12.3
- sqlparse ==0.2.4 # fix error when migration
Settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'real_estate',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': MONGO_URI
        }
    }
}
```
For PostgreSQL as default database:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'real_estate',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost'
    }
}
```

```
Flow: 
- settings.py (INSTALLED_APPS > DATABASES (EMAIL CONFIG))
- models.py (database model) -> migrations
- templastes, html (new) (Create template)
  - base.html: Behave as a template
- app/admin.py: Admin Configuration
- static /media-css-js: Frontend
- views.py (create view)
- urls.py (new) (create route)
- utils/forms.py (new) (create Form to get data)
- views.py (Insert data to database)
```

```
# Create admin
python manage.py createsuperuser
```

## Pillow 9.2.0

Pillow in a Django project helps handle image uploads, process images, create thumbnails, and perform various image-related tasks.

## Frontend

**Bootstrap links:**
- [Bootstrap](https://getbootstrap.com/)
- [Bootstrap navigation bar](https://getbootstrap.com/docs/4.0/components/navbar/)
- [Bootstrap cards](https://getbootstrap.com/docs/4.0/components/card/)
- [Bootstrap pricing cards](https://getbootstrap.com/docs/4.0/examples/pricing/)


**Bootswatch link:**
```Markdown
Free Bootstrap theme
```
- [Bootswatch](https://bootswatch.com/)

**Font awesome links:**
- [Font awesome CDN](https://www.w3schools.com/icons/fontawesome_icons_intro.asp)
- [Font awesome icons](https://fontawesome.com/v4/icons/)