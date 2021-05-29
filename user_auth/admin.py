from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'phone', 'role', 'date_joined']
    list_filter = ['is_superuser', 'role']
    search_fields = ['username']
    # paginator = 30
    fieldsets = (
        (None,
         {'fields': ('username', 'email', 'password')}),
        (('Личная информация'),
         {'fields': (
             'first_name', 'last_name', 'phone', 'role')}),
        (('Права доступа'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        ('Дата и время', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'username', 'first_name', 'last_name', 'phone', 'role',  'password1',
                'password2', 'is_active',
                'is_staff', 'is_superuser'),
        }),
    )




from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
from allauth.account.admin import EmailAddress


admin.site.unregister(EmailAddress)
admin.site.unregister(Group)
admin.site.unregister(Site)
