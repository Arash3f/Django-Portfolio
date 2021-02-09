from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='account'

urlpatterns = [
    # unComment after create super user
    # path('', views.site_page , name='site_page'),
    # path('about/', views.about_page , name='about_page'),
    # path('services/', views.services_page , name='services_page'),
    # path('contact/', views.contact.as_view() , name='contact_page'),
    # path('blog/', views.blog , name='blog'),
    # path('blog/<slug:tag_slug>/' , views.blog , name='main_site_tag'),
    # path('<int:year>/<int:month>/<int:day>/<slug:post>/' , views.detail_post,name='detail'),
]