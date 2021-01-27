from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from django.contrib import admin

fields = list(UserAdmin.fieldsets)
fields[1] = ('Personal info', {'fields': ('first_name','last_name','email','phone',
                                            'job','Date','Location','picture','summery',
                                            'about','end_about_me','total_project','total_volunteers','total_donation',
                                            'instagram','github','telegram','twitter')})
UserAdmin.fieldsets = tuple(fields)
# UserAdmin.fieldsets += ('New fields set', {'fields': ('first_name','last_name','email','picture', 'summery','job','Date', 'phone',
                                            # 'Location','github','telegram','twitter','instagram',
                                            # 'about','total_project','total_volunteers','total_donation',
                                            # 'end_about_me')}),
                                            
                                            
admin.site.register(models.User, UserAdmin)



@admin.register(models.project)
class projectAdmin(admin.ModelAdmin):
    list_display  = ['__str__','tags_name_admin']
    list_filter = ['tag']
    
    
@admin.register(models.skill)
class skillAdmin(admin.ModelAdmin):
    list_display  = ['__str__','amount']
    
    
    
@admin.register(models.experiences)
class experiencesAdmin(admin.ModelAdmin):
    list_display  = ['__str__' , 'Date']
    list_filter = ['Date']
    
    
@admin.register(models.services)
class servicesAdmin(admin.ModelAdmin):
    list_display  = ['__str__' ]
    
@admin.register(models.messages)
class messagesAdmin(admin.ModelAdmin):
    list_display  = ['__str__' ]