from .views import crudViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = []

router = DefaultRouter()
router.register(r'usuario', crudViewSet, basename='crud')

urlpatterns += router.urls