from django.urls import path
from .views import CategoryViewSet, ProductViewSet, ProductDetailView, OrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', CategoryViewSet)
router.register(r'product', ProductViewSet)
router.register(r'detail/<int:pk>/',  ProductDetailView)
router.register(r'order',  OrderViewSet)


urlpatterns = router.urls
