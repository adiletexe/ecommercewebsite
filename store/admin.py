from django.contrib import admin
from .models import Product
# Register your models here.
class AdminPage(admin.ModelAdmin):
    list_display = ('title', 'slug', 'price', 'stock', 'category', 'date_modified', 'is_available')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Product, AdminPage)