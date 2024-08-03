from django.contrib import admin
from todolist.models import Task, Comment, Tag
from django.contrib.auth.admin import UserAdmin
from users.models import User


# admin.site.register(Task)
# или по красоте:

class CommentInLine(admin.TabularInline):
    model = Comment


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'owner', 'due_date',)
    list_filter = ('status', 'owner', 'due_date',)
    search_fields = ('name', 'description',)

    inlines = [CommentInLine]


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    search_fields = ('email',)
    ordering = ('email',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)
    # list_filter = ('status', 'owner', 'due_date')
    search_fields = ('name',)
