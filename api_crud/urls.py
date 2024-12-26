from .views import crudUsuarioViewSet, EjerciciosViews
from rest_framework.routers import DefaultRouter
from django.urls import path
urlpatterns = [
    path('palindromo', EjerciciosViews.isPalindromo, name='isPalindromo'),
]

router = DefaultRouter()
router.register(r'usuario', crudUsuarioViewSet, basename='crudUsuarioViewSet')

urlpatterns += router.urls