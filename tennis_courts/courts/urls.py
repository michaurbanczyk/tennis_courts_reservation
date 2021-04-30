from django.urls import path
from . import views

app_name = 'courts'

urlpatterns = [
    path('', views.home, name="home"),
    path('regions/', views.regions_view, name="regions")
]
