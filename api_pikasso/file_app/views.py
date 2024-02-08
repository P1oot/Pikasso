from rest_framework import viewsets, mixins
from .models import File
from .serializers import CreateFileSerializer, ListFileSerializer


class CreateFileViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = File.objects.all()
    serializer_class = CreateFileSerializer


class ListFileViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = File.objects.all()
    serializer_class = ListFileSerializer
