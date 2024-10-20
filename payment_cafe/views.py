from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .serializers import PaymentSerializer
from rest_framework import filters
from .models import Payment

# Create your views here.
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    pagination_classes = [StandardResultsSetPagination]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'payment_date']