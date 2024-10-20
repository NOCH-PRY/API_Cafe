from rest_framework.routers import DefaultRouter
from .views import OrderItemViewSet

router = DefaultRouter()

router.register(r'crud_orderItems', OrderItemViewSet, basename="crudOrderItems")

urlpatterns = router.urls