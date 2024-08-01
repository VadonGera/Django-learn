from django.contrib import admin
from todolist.models import Task

# admin.site.register(Task)
# или по красоте:
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'owner', 'due_date')
    list_filter = ('status', 'owner', 'due_date')
    search_fields = ('name', 'description')
