from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User

admin.site.register(User)

# class CustomUserAdmin(UserAdmin):
#     list_display = ['username', 'email', 'is_active', 'is_superuser'] 
#     list_filter = ['is_active'] 

# admin.site.register(User, CustomUserAdmin)
