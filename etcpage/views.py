from django.shortcuts import render

# Create your views here.
from product.models import Category, Product


def home(request):
    return render(request, 'etcpage/home.html', context={
        'root_categories': Category.objects.filter(parent__isnull=True).order_by('priority'),
        'products': Product.objects.all().order_by('-score', '-created_at')[:5]
    })