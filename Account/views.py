from Account import models
from django.shortcuts import render
from taggit.models import Tag



def site_page(request):
    html = 'main.html'
    
    user        = models.User.objects.all()[0]
    skill       = models.skill.objects.all().order_by('-amount')
    experiences = models.experiences.objects.all().order_by('Date')
    tags        = Tag.objects.all()
    projects    = models.project.objects.all()
    services    = models.services.objects.all()
    
    data = {    'user'  :user ,
                'skills' :skill , 
                'exps'   :experiences ,
                'projs' :projects ,
                'tags' :tags ,
                'services' : services
            }
    
    return render(request,html,data)

def about_page(request):
    html = 'about.html'
    
    user        = models.User.objects.all()[0]
    skill       = models.skill.objects.all().order_by('-amount')
    
    data = {    'user'  :user ,
                'skills' :skill 
            }
    
    return render(request,html,data)


def services_page(request):
    html = 'services.html'
    
    user        = models.User.objects.all()[0]
    services    = models.services.objects.all()
    
    data = {    'user'  :user ,
                'services' : services
            }
    
    return render(request,html,data)

def contact_page(request):
    html = 'contact.html'
    
    user        = models.User.objects.all()[0]
    
    data = {    'user'  :user 
            }
    
    return render(request,html,data)