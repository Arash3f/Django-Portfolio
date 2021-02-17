from django import forms
from Account import models
from django.core.exceptions import ValidationError
from django.db.models import Q
class registerform(forms.ModelForm):
    class Meta:
        model = models.User
        fields =('username', 'first_name', 'last_name', 'email' ,'password')
        widgets = {
            'username'    :     forms.TextInput(attrs={'class':"input--style-4" , "type":"text"  , "name":"username" }),
            'first_name'  :     forms.TextInput(attrs={'class':"input--style-4" , "type":"text" , "name":"first_name"}),
            'last_name'   :     forms.TextInput(attrs={'class':"input--style-4" , "type":"text", "name":"last_name"  }),
            'email'       :     forms.EmailInput (attrs={'class': "input--style-4" , "type":"email" , "name":"email"   }),
            'password'    :     forms.PasswordInput (attrs={'class': "input--style-4" , "type":"password" , "name":"password"   }),
        }
    def clean(self):
        cd = self.cleaned_data
        username = cd.get('username')
        first_name= cd.get('first_name')
        last_name= cd.get('last_name')
        password = cd.get('password')
        email = cd.get('email')
        if first_name=="" :
            raise ValidationError("enter first name plese")
        elif last_name=="":
            raise ValidationError("enter last name plese")
        elif email=="":
            raise ValidationError("enter email plese")
        elif models.User.objects.filter(Q(username=username)|Q(email=email)):
            raise ValidationError("error")
        return cd


 