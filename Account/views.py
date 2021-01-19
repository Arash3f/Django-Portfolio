
from Account import models
from django.shortcuts import render
from taggit.models import Tag



def site_page(request):
    html = 'main.html'
    
    user        = models.User.objects.all()[0]
    skill       = models.skill.objects.all()
    experiences = models.experiences.objects.all()
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