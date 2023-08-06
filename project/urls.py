from django.contrib import admin
from django.urls import path, include

# static media url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),  # Project-level URL
    path('listings/', include('listings.urls')),  # Project-level URL
    path('admin/', admin.site.urls),  # Project-level URL
    path('accounts/', include('accounts.urls')),  # Project-level URL
    path('contacts/', include('contacts.urls'))
]

# Setting unique image URL
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
