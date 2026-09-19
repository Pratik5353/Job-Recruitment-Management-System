from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Profile", {"fields": ("role","phone","headline","location","company")}),)
    list_display = ("username","email","role","company","is_staff")
    list_filter = ("role","is_staff","is_active")
