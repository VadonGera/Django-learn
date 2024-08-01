from django.contrib import admin
from todolist.models import Task, Comment


# admin.site.register(Task)
# или по красоте:

class CommentInLine(admin.TabularInline):
    model = Comment


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'owner', 'due_date')
    list_filter = ('status', 'owner', 'due_date')
    search_fields = ('name', 'description')

    inlines = [CommentInLine]
