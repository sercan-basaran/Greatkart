from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,UserProfile
class AccountAdmin(UserAdmin):
    list_display=('first_name','last_name',"email","username",'date_joined','last_login','role','is_admin','is_staff','is_active',)
    ordering = ('-date_joined',)
    list_display_links=("first_name","last_name","email")
    readonly_fiels=('date_joined','last_login')
    
    #passwordun değiştirilmesi için
    filter_horizontal=() 
    list_filter=()
    fieldsets=()
    
    
class UserProfilesAdmin(admin.ModelAdmin):
    list_display=('user','city','state','country','phone_number')
    list_display_links=('user',)
    search_fields=('user','city','state','country')
    list_per_page=25
    





        
    
admin.site.register(User,AccountAdmin)    
admin.site.register(UserProfile)        
    
    
