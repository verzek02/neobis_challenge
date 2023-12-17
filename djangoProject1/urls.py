from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from neobis_challenge.views import CategoryViewSet, ProductViewSet, ProductDetailViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('neobis_challenge.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
