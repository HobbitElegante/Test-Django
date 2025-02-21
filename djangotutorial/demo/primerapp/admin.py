from django.contrib import admin
from .models import TodoItem
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "priority", "joined_date")


admin.site.register(TodoItem, TodoAdmin)