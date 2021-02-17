

from django.shortcuts import redirect, render , get_object_or_404
from django.template import RequestContext
from django.template import loader
from . import forms
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib.auth.decorators import login_required
from Account import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin

def handler404(request, exception):
    template_name="404.html"
    return render(request,template_name)

class register(View):
    template_name="registration/register.html"
    form        = forms.registerform()
    
    def get(self, request):
        data = {
                    'form'  :self.form
                }
        return render(request,self.template_name,data)

    def post(self, request):
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')

        form = forms.registerform(request.POST)
        if username=="" or first_name=="" or last_name=="" or email=="" or password=="" :
            return render(request,"404.html")
        if form.is_valid():
            form.save()
            form =forms.registerform()
            return redirect('/')
        data = { 
                    'form'  :form
                }
        return render(request,self.template_name,data)


class dashboard(LoginRequiredMixin,View):
    template_name="dashboard.html"
    login_url = '/account/login/'
    
    def get(self, request):
        return render(request,self.template_name)

    def post(self, request):
        
        first_name=request.POST.get('name')
        lastname=request.POST.get('last_name')
        password=request.POST.get('password')
        re_password=request.POST.get('re_password')
        email=request.POST.get('email')
        if first_name=="" or lastname=="" or password=="" or re_password=="" or email=="" :
            return render(request,"404.html")
        if password!=re_password:
            return render(request,"404.html")
        else:
            up = get_object_or_404(models.User,username=request.user.username)
            up.first_name=first_name
            up.last_name=lastname
            up.password=make_password(password)
            up.email=email
            up.save()
            return render(request,self.template_name)
            

@login_required(login_url='/account/login/')
def comments(request):
    comments = models.comments.objects.filter(user=request.user)
    data = {
        "comments":comments
    }
    template_name="comments.html"
    return render(request,template_name,data)