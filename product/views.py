from django.shortcuts import render

from product.models import Product


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'product/detail_does_not_exist.html', status=404)

    return render(request, 'product/detail.html', context={
        'product': product
    })
