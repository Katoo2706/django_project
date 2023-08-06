from django.urls import path

from . import views

# /listing/listing_id
urlpatterns = [
    path('contact', views.contact, name='contact')
]