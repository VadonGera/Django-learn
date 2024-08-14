from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User, CustomUserManager


# admin.site.register(User)

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):   # (UserAdmin)
    model = User
    list_display = ('email', 'is_active', 'is_active',)
    # list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    search_fields = ('email',)
    ordering = ('email',)
