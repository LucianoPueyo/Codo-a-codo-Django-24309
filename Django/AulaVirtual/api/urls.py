from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'Alumnos', views.AlumnosViewSet, basename='alumno')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework')
]