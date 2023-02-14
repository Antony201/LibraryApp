from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from library import settings

from rest_framework import routers

from books.views import BookViewSet


router = routers.DefaultRouter()

router.register(r'books', BookViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)