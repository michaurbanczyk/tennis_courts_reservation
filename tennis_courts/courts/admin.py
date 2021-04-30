from django.contrib import admin
from .models import Region, City


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', )
    ordering = ('name', )


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', )
    ordering = ('name',)

