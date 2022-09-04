from django.contrib import admin
from .models import Categories

# Register your models here.
class AdminPage1(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title', 'slug')
admin.site.register(Categories, AdminPage1)