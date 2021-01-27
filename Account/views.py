from Account import models
from django.shortcuts import render
from taggit.models import Tag
from . import forms
from django.views import View



def site_page(request):
    html = 'main.html'
    
    user        = models.User.objects.all()[0]
    skill       = models.skill.objects.all().order_by('-amount')
    experiences = models.experiences.objects.all().order_by('Date')
    tags        = Tag.objects.all()
    projects    = models.project.objects.all()[:6]
    services    = models.services.objects.all()[:6]
    
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

class contact(View):
    html = 'contact.html'
    form = forms.messageform()
    user        = models.User.objects.all()[0]
    def get(self, request):
        data = {    'user'  :self.user ,
                    'form'  :self.form
                }
        return render(request,self.html,data)
    def post(self, request):
        form = forms.messageform(request.POST)
        if form.is_valid():
            print(form.is_valid())
            form.save()
            form =forms.messageform()
        data = {    'user'  :self.user ,
                    'form'  :form
                }
        return render(request,self.html,data)