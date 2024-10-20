from rest_framework.routers import DefaultRouter
from .views import PromotionViewSet

router = DefaultRouter()
router.register(r'crud_promotions', PromotionViewSet, basename="crudPromotions")

urlpatterns = router.urls