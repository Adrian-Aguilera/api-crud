from .views import crudViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = []

router = DefaultRouter()
router.register(r'crud', crudViewSet, basename='crud')

urlpatterns += router.urls