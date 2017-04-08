from django.conf.urls import url
from product import views

urlpatterns = [
    url(r'^products/(?P<product_id>\d+)$', views.product_detail),
]

# http://127.0.0.1:8000/product/products/1