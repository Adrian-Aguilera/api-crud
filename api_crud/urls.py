from .views import crudUsuarioViewSet, EjerciciosViews
from rest_framework.routers import DefaultRouter
from django.urls import path
urlpatterns = [
    path('es-palindromo', EjerciciosViews.isPalindromo, name='isPalindromo'),
    path('fizzbuzz', EjerciciosViews.fizzbuzz, name='fizzbuzz'),
]

router = DefaultRouter()
router.register(r'usuario', crudUsuarioViewSet, basename='crudUsuarioViewSet')

urlpatterns += router.urls