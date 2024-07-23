from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework import routers
from tb_siswa.views import SiswaViewSet

router = routers.DefaultRouter()
router.register(r'siswa', SiswaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('tb_siswa.urls')),
]