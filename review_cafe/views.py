from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .serializers import ReviewSerializer
from rest_framework import filters
from .models import Review

# Create your views here.
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_classes = [StandardResultsSetPagination]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id',]