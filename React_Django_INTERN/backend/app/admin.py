from django.contrib import admin
from .models import Custom_User, User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'password', 'otp']

@admin.register(Custom_User)
class C_User(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'job', 'position', 'department']