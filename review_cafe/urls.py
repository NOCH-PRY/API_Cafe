from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet

router = DefaultRouter()

router.register(r'crud_reviews', ReviewViewSet, basename='crudReviews')

urlpatterns = router.urls