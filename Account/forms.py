from django import forms
from . import models
from django.core.exceptions import ValidationError
class messageform(forms.ModelForm):
    class Meta:
        model = models.messages
        fields ='__all__'
        widgets = {
            'name'   : forms.TextInput(attrs={'class':"form-control" , "type":"text" , "id":"name" , "name":"name" , "placeholder":"Enter your name"}),
            'email'  : forms.TextInput(attrs={'class':"form-control" , "type":"email" , "id":"email" , "name":"email" , "placeholder":"Enter your email"}),
            'subject': forms.TextInput(attrs={'class':"form-control" , "type":"text" , "id":"subject" , "name":"subject" , "placeholder":"Enter subject"}),
            'mes'    : forms.Textarea(attrs={'class': "form-control" , "id":"message" , "name":"message" , "placeholder":"Enter message"}),
        }
    def clean(self):
        cd = self.cleaned_data
        email = cd.get('email')
        name = cd.get('name')
        subject = cd.get('subject')
        mes = cd.get('mes')
        if email==None :
            raise ValidationError("enter email plese")
        elif name==None:
            raise ValidationError("enter name plese")
        elif mes==None:
            raise ValidationError("enter mes plese")
        elif subject==None:
            raise ValidationError("enter subject plese")
        return cd
    
class CommentFrom(forms.ModelForm):
    class Meta:
        model = models.comments
        fields =('body',)
        widgets = {
            'body'   : forms.Textarea(attrs={'class':"form-control" , "type":"text" , "id":"name" , "name":"message" , "placeholder":"Messege"}),
        }