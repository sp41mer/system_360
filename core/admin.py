from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.forms import ChangeUserForm, CreateUserForm
from core.models import User


class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'patronymic_name', 'last_name', 'department', 'password1', 'password2'),
        }),
    )

    list_display = (
        'first_name',
        'last_name',
        'department',
        'is_staff',
        'is_superuser',
    )

    form = ChangeUserForm
    add_form = CreateUserForm

admin.site.register(User, CustomUserAdmin)
