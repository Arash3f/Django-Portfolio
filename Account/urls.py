from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.site_page , name='main_page'),
    path('about/', views.about_page , name='about_page'),
    path('services/', views.services_page , name='services_page'),
    path('contact/', views.contact.as_view() , name='contact_page'),
]