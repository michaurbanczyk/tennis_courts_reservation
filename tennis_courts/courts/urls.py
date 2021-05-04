from django.urls import path
from . import views

app_name = 'courts'

urlpatterns = [
    path('', views.home, name="home"),
    path('clubs/', views.clubs_view, name="clubs")
]
