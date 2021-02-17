from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils import timezone

class User(AbstractUser):

    picture_main         = models.ImageField  ( 'Picture1' , upload_to='user_pictures/' , blank=True , null=True ,help_text="485x600")
    picture_blog        = models.ImageField  (  'Picture2' , upload_to='user_pictures/' , blank=True , null=True ,help_text="120x120")
    summery         = RichTextField()
    about           = RichTextField()
    end_about_me    = RichTextField()
    job             = models.CharField   ( 'Job'       , max_length=30 , blank=True , null=True)
    date_of_birth   = models.DateField   ( 'Date of birth' , blank=True , null=True)
    phone           = models.CharField   ( 'Phone'     , max_length=11 , blank=True , null=True)
    Location        = models.CharField   ( 'Location'  , max_length=30 , blank=True , null=True)
    github          = models.CharField   ( 'github'    , max_length=100 , blank=True , null=True)
    skype        = models.CharField   ( 'skype'  , max_length=100 , blank=True , null=True)
    twitter         = models.CharField   ( 'twitter'   , max_length=100 , blank=True , null=True)
    instagram       = models.CharField   ( 'instagram' , max_length=100 , blank=True , null=True)
    total_project   = models.IntegerField('total project'    , default=0 , blank=True , null=True)
    total_volunteers= models.IntegerField('total volunteers' , default=0 , blank=True , null=True)
    total_donation  = models.IntegerField('total donation'   , default=0 , blank=True , null=True)

class skill(models.Model):
    title  = models.CharField   ( 'Title'  , max_length=30 , blank=True , null=True)
    amount = models.IntegerField( 'amount' , default=0 , blank=True , null=True)
    
    def __str__(self):
        return f"{self.title}"
    
class experiences(models.Model):
    title     = models.CharField( 'Title' , max_length=30 , blank=True , null=True)
    about     = models.TextField( 'About',max_length=100 , blank=True  , null=True )
    Date      = models.DateField( 'Date' , blank=True , null=True)
    
    def __str__(self):
        return f"{self.title}"
    
    def format_date(self):
        return self.Date.strftime("%Y/%m/%d")
    
class services(models.Model):
    title     = models.CharField( 'Title' , max_length=30 , blank=True , null=True)
    about     = RichTextField()
    
    def __str__(self):
        return f"{self.title}"
    
class messages(models.Model):
    name        = models.CharField( 'name' , max_length=30 , blank=True , null=True)
    email       = models.EmailField('email' , blank=True , null=True )
    subject     = models.CharField( 'subject' , max_length=30 , blank=True , null=True)
    mes         = models.TextField( 'mesmessage' , max_length=300 , blank=True , null=True)
    
    def __str__(self):
        return f"{self.name}"
    
class comments(models.Model):
    user       = models.ForeignKey(User , on_delete=models.CASCADE , related_name='user_comment')
    Date      = models.DateField( 'Date' , auto_now_add=True ,  blank=True , null=True)
    body       = models.TextField( 'Body', blank=True , null=True)
    post       = models.ForeignKey('project' , on_delete=models.CASCADE , related_name='post_comment')

    def format_date(self):
        return self.Date.strftime("%Y/%m/%d")
    
class views(models.Model):
    ip = models.CharField('ip' ,max_length=30 ,blank=True , null=True )
    post = models.ForeignKey('project' , on_delete=models.CASCADE , related_name='view_post')
    
class project(models.Model):
    title          = models.CharField( 'title' , max_length=30 , blank=True , null=True)
    summery         = RichTextField()
    body           = RichTextField()
    picture_main     = models.ImageField( 'picture1' , upload_to='projects/' , blank=True , null=True ,help_text="555x471")
    picture_blog     = models.ImageField( 'picture2' , upload_to='projects/' , blank=True , null=True ,help_text="555x280")
    slug         = models.SlugField()
    tag          = TaggableManager()
    created_at  = models.DateTimeField( 'created_at' , auto_now_add=True )
    updated_at  = models.DateTimeField( 'updated_at' , auto_now=True)
    view        = models.IntegerField('view'  ,default=0 ,blank=True ,null=True)
    author       = models.ForeignKey(User , on_delete=models.CASCADE , related_name='projectuser')
    publish    = models.DateTimeField(default=timezone.now)
    
    def format_date(self):
        return self.created_at.strftime("%Y/%m/%d")
        
    def get_absolute_url(self):
        return reverse('account:detail',args=[self.publish.year,self.publish.month,self.publish.day,self.slug])
    
    def comment1(self):
        comment_number = comments.objects.filter(post__id=self.id).count()
        return comment_number
    
    def view_plus(self,request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        view_list =[]
        for i in self.view_post.all():
            view_list.append(i.ip)
        if ip not in view_list:
            post = project.objects.get(id=self.id)
            new = views.objects.create(ip=ip , post=post)
            new.save()
            self.view +=  1
            self.save()
    
    def __str__(self):
        return f"{self.title}"
    
    def tags_name(self):
        return (" ".join(i.name for i in self.tag.all()))
    
    def tags_name_admin(self):
        return (", ".join(i.name for i in self.tag.all()))
    tags_name_admin.short_description = "tags"
    

    
    

    
    
    
    
    