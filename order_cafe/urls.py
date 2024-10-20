from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

router = DefaultRouter()
router.register(r'crud_orders', OrderViewSet, basename='crudOrders')

urlpatterns = router.urls