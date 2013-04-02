from django.contrib import admin
from models import Product, Category
from forms import ProductAdminForm


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

    list_display = ('name', 'price', 'old_price', 'created_at', 'update_at',)
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['name', 'description']

    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['name', 'description']

    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
