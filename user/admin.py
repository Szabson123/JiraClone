from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('email', 'is_staff', 'is_active',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal', {'fields': ('first_name', 'last_name')}),  
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    
    
    search_fields = ('email',)
    ordering = ('id',)

admin.site.register(CustomUser, CustomUserAdmin)