from django.urls import path
from .views import index, add_siswa, delete_siswa

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_siswa, name='add_siswa'),
    path('delete/<int:id>/', delete_siswa, name='delete_siswa'),
]
