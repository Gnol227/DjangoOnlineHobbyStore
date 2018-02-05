from django.contrib import admin
from .models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} #the value of 'slug' is automatic set by the value of 'name'
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'status', 'created', 'updated']
    list_filter = ['status', 'created', 'updated']
    list_editable = ['price', 'stock', 'status']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)
