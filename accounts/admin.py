from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Accounts

class AdminPage(UserAdmin):
    list_display = ('username', 'firstname', 'secondname', 'date_signed', 'date_logged', 'is_active')
    list_display_links = ('username', 'firstname', 'secondname')
    ordering = ('-date_signed',)
    readonly_fields = ('date_signed', 'date_logged', 'is_active')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
# Register your models here.
admin.site.register(Accounts, AdminPage)