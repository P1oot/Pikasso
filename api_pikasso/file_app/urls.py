from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CreateFileViewSet, ListFileViewSet

router = SimpleRouter()
router.register('upload', CreateFileViewSet)
router.register('files', ListFileViewSet)

urlpatterns = [
    path('', include(router.urls))
]
