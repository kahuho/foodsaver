from django.contrib import admin
# Register your models here.
from django.contrib.gis.admin import OSMGeoAdmin

from .models import Products


@admin.register(Products)
class Products_Admin(OSMGeoAdmin):
    list_display = ("title", "user", "published_date", "location")
