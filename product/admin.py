from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

from product.models import Category, DateRangeDiscount
from product.models import Product

admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    pass

admin.site.register(DateRangeDiscount)
