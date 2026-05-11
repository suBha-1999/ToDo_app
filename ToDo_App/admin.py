from django.contrib import admin
from .models import Task


# for view status in admin page
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'updated_at') # Both variables taken from models.py attributes.
    search_fields = ['task'] # here you put list or tuple as per the rule.


# Register your models here.
admin.site.register(Task, TaskAdmin) # here we want to show task status in admin field. so need to put a class TaskAdmin ------>