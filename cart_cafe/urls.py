from rest_framework.routers import DefaultRouter
from .views import CartViewSet

router = DefaultRouter()

router.register(r'crud_cart', CartViewSet, basename="cruCart")

urlpatterns = router.urls