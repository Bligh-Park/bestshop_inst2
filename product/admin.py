from django.contrib import admin

# Register your models here.
from product.models import Category, DateRangeDiscount
from product.models import Product

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(DateRangeDiscount)
