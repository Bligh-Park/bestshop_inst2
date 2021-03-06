from django.http import Http404
from django.shortcuts import render

from product.models import Product, Category


def product_detail(request, product_id):

    # from django.conf import settings
    # import boto3
    # client = boto3.client('sns',
    #                       aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    #                       aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    #                       region_name='ap-northeast-1')
    #
    # client.publish(
    #     PhoneNumber='+821099799082',
    #     Message='test',
    # )
    #
    # from django.core.mail import send_mail
    # send_mail(subject='test', message='This is AWS test mail.', from_email='sy131.park@gmail.com',
    #           recipient_list=[
    #               'sy131.park@gmail.com'
    #           ])

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'product/detail_does_not_exist.html', status=404)

    return render(request, 'product/detail.html', context={
        'product': product
    })


def product_list(request):
    try:
        category = Category.objects.get(id=request.GET.get('category_id'))
    except Category.DoesNotExist:
        raise Http404()

    return render(request, 'product/list.html', context={
        'category': category,
        'products': Product.objects.filter(
            categories__id__in=[category.id for category in category.all_parent_set]
        ).distinct()
    })
