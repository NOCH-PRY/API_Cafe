from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet

router = DefaultRouter()
router.register(r'crud_payment', PaymentViewSet, basename="crudPayment")

urlpatterns = router.urls