from django.urls import path

from . import views

# /listing/listing_id
urlpatterns = [
    path('', views.index, name='listings'),    # url parent /listing
    path('<int:listing_id>', views.listing, name='listing'),  # <int:listing_id>
    path('search', views.search, name='search')  # listing/search
]