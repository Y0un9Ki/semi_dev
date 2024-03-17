from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (None, {'fields': ('username', 'password')}),
        ('개인정보', {'fields': ('first_name', 'last_name', 'email')}),
        ('추가필드', {'fields': ('location',)}),
        (
            '권한',
                {
                    'fields': (
                        'is_activate',
                        'is_staff',
                        'is_superuser',
                    )
                }
        ),
    ]