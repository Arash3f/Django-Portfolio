from django.urls import path
from . import views

urlpatterns = [
    path('', views.site_page , name='main_page'),
]