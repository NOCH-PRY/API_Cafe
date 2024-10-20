from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .serializers import OrderSerializer
from rest_framework import filters
from .models import Order


# Create your views here.
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_classes = [StandardResultsSetPagination]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', '^status']