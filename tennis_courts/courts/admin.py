from django.contrib import admin

from courts.models import Club, City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'zip_code', 'city')
    ordering = ('name', )

