from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route

from product.models import Product
from product.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    @list_route(methods=['GET'], url_path='test-items')
    def test_items(self, request):
        return Response([])

    @detail_route(methods=['GET'])
    def likes(self, request, pk):
        obj = self.get_object()

        return Response({'count':obj.name})
