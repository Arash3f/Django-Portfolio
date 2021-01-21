from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
class User(AbstractUser):
    
    picture         = models.ImageField  ( 'picture' , upload_to='user_pictures/' , blank=True , null=True )
    summery         = RichTextField()
    job             = models.CharField   ( 'job' , max_length=30 , blank=True , null=True)
    Date            = models.DateField   ( 'Date' , blank=True , null=True)
    phone           = models.CharField   ( 'phone' , max_length=11 , blank=True , null=True)
    Location        = models.CharField   ( 'Location' , max_length=30 , blank=True , null=True)
    github          = models.CharField   ( 'github' , max_length=100 , blank=True , null=True)
    telegram        = models.CharField   ( 'telegram' , max_length=100 , blank=True , null=True)
    twitter         = models.CharField   ( 'twitter' , max_length=100 , blank=True , null=True)
    instagram       = models.CharField   ( 'instagram' , max_length=100 , blank=True , null=True)
    about           = RichTextField()
    total_project   = models.IntegerField('total project' , default=0 , blank=True , null=True)
    total_volunteers= models.IntegerField('total volunteers' , default=0 , blank=True , null=True)
    total_donation  = models.IntegerField('total donation' , default=0 , blank=True , null=True)
    end_about_me    = RichTextField()
    
    
class skill(models.Model):
    title  = models.CharField   ( 'name' , max_length=30 , blank=True , null=True)
    amount = models.IntegerField('amount' , default=0 , blank=True , null=True)
    
    def __str__(self):
        return f"{self.title}"
    
class experiences(models.Model):
    title     = models.CharField( 'title' , max_length=30 , blank=True , null=True)
    about     = models.TextField('about',max_length=100 , blank=True  , null=True )
    Date      = models.DateField( 'Date' , blank=True , null=True)
    
    def __str__(self):
        return f"{self.title}"
    
    
class project(models.Model):
    title       = models.CharField( 'title' , max_length=30 , blank=True , null=True)
    title_2     = RichTextField()
    picture     = models.ImageField( 'picture' , upload_to='user_pictures/' , blank=True , null=True )
    tag         = TaggableManager()
    
    
    def __str__(self):
        return f"{self.title}"
    
    def tags_name(self):
        return (" ".join(i.name for i in self.tag.all()))
    
    def tags_name_admin(self):
        return (", ".join(i.name for i in self.tag.all()))
    tags_name_admin.short_description = "tags"
    
class services(models.Model):
    title     = models.CharField( 'title' , max_length=30 , blank=True , null=True)
    about     = RichTextField()
    
    def __str__(self):
        return f"{self.title}"
    
    
    