from .views import crudUsuarioViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = []

router = DefaultRouter()
router.register(r'usuario', crudUsuarioViewSet, basename='crudUsuarioViewSet')

urlpatterns += router.urls