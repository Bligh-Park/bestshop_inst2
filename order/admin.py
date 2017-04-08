from django.contrib import admin

from order.models import Cart, OrderProductItem
from order.models import Order

admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderProductItem)
