from django.contrib import admin
from .models import Product
# Register your models here.

class Adminslug(admin.ModelAdmin):
    list_display = ('products_name', 'price', 'stock', 'category', 'created_date', 'modified_date')
    prepopulated_fields = {'slug':('products_name',)}




admin.site.register(Product,Adminslug)
