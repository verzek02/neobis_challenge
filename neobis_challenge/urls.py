from django.urls import path
from .views import CategoryViewSet, ProductViewSet, ProductDetailViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)
router.register(r'product_detail', ProductDetailViewSet)


urlpatterns = router.urls
