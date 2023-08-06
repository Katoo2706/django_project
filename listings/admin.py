from django.contrib import admin
from .models import Listing


# Register your models here.
@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'is_published', 'list_date', 'realtor',)
    list_display_links = ('id', 'title')  # link above
    search_fields = ('realtor', )
    list_filter = ('is_published',)
    list_editable = ('is_published',)
    list_per_page = 25
