from django.contrib import admin
from .models import Project , Experience , ContactMessage
# core/admin.py
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "featured")
    list_filter = ("featured",)
    search_fields = ("title", "tech_stack")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "company", "start_date", "end_date")
    search_fields = ("company", "role")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    readonly_fields = ("name", "email", "message", "created_at")

# Register your models here.
