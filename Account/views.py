from Account import models
from django.shortcuts import get_object_or_404, render
from taggit.models import Tag
from . import forms
from django.views import View
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
# python manage.py migrate --run-syncdb



def site_page(request):
    html = 'main.html'
    user        = get_object_or_404(models.User,id=1)
    skills      = models.skill.objects.all().order_by('-amount')
    experiences = models.experiences.objects.all().order_by('-Date')
    tags        = Tag.objects.all()
    projects    = models.project.objects.all().order_by('-created_at')[:6]
    services    = models.services.objects.all()[:3]
    
    data = {    'user'  :user ,
                'skills' :skills , 
                'exps'   :experiences ,
                'projs' :projects ,
                'tags' :tags ,
                'services' : services
            }
    
    return render(request,html,data)

def about_page(request):
    html = 'about.html'
    user        = get_object_or_404(models.User,id=1)
    skill       = models.skill.objects.all().order_by('-amount')
    
    data = {    'user'  :user ,
                'skills' :skill 
            }
    
    return render(request,html,data)

def services_page(request):
    html = 'services.html'
    user        = get_object_or_404(models.User,id=1)
    services    = models.services.objects.all()
    
    data = {    'user'  :user ,
                'services' : services
            }
    
    return render(request,html,data)

class contact(View):
    html        = 'contact.html'
    form        = forms.messageform()
    user        = get_object_or_404(models.User,id=1)
    
    def get(self, request):
        data = {    'user'  :self.user ,
                    'form'  :self.form
                }
        return render(request,self.html,data)
    
    def post(self, request):
        form = forms.messageform(request.POST)
        if form.is_valid():
            form.save()
            form =forms.messageform()
        data = {    'user'  :self.user ,
                    'form'  :form
                }
        return render(request,self.html,data)
    
def contact_page(request):
    html        = 'contact.html'
    form        = forms.messageform(request.POST or None)
    user        = get_object_or_404(models.User,id=1)
    if form.is_valid():
        form.save()
        form =forms.messageform()
    data = {    'user'  :user ,
                'form'  :form
            }
    return render(request,html,data)

def blog(request, tag_slug=None):
    html        = 'blog.html'
    tag         = None
    user        = get_object_or_404(models.User,id=1)
    tags        = Tag.objects.all()
    projects    = models.project.objects.all()
    last_pro    = models.project.objects.all()[:5]
    
    if tag_slug:
        tag      = get_object_or_404(Tag, slug=tag_slug)
        projects = projects.filter(tag__in=[tag])
        
    paginator = Paginator(projects , 1 )
    page = request.GET.get('page')
    
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
        
    data = {    'user'  :user ,
                'projs' :projects ,
                'tags' :tags ,
                "last_pro":last_pro , 
                'page':page,
            }
    
    return render(request,html,data);

def detail_post(request,year,month,day,post):
    tags        = Tag.objects.all()
    last_pro    = models.project.objects.all()[:5]
    author      = request.user
    user        = get_object_or_404(models.User,id=1)
    projs       = get_object_or_404(models.project, slug=post , publish__year=year, publish__month=month, publish__day=day)
    projs.view_plus(request)
    comments    = models.comments.objects.filter(post = projs)
    new_comment = None
    if request.method == 'POST':
        comment_form = forms.CommentFrom(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = projs
            new_comment.user = author
            new_comment.save()
            comment_form = forms.CommentFrom()
    else:
        comment_form = forms.CommentFrom()
        
    paginator = Paginator(comments , 10 )
    page = request.GET.get('page')
    
    try:
        com = paginator.page(page)
    except PageNotAnInteger:
        com = paginator.page(1)
    except EmptyPage:
        com = paginator.page(paginator.num_pages)
        
    # post_tags_ids = poste.tag.values_list('id', flat=True)
    # similar_post = Posts.objects.filter(tag__in=post_tags_ids).distinct().exclude(id=poste.id)
    # similar_post = similar_post.annotate(same_tag=Count('tag')).order_by('-same_tag','-publish')[:4] 
    
    data = {    'user'  :user ,
                'pro' :projs ,
                'comments':com,
                'page':page,
                'comment_form':comment_form,
                "last_pro":last_pro , 
                'tags' :tags ,
            }
    
    return render(request, 'details.html' , data)























