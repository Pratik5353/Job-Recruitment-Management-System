from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title","company","work_type","experience","is_active","created_at")
    list_filter = ("work_type","employment_type","experience","is_active")
    search_fields = ("title","company","skills","location")
