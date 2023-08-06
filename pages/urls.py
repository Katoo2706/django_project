from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),  # home pages, not /
    path('about/', views.about, name='about')
]