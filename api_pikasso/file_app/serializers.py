from rest_framework import serializers
from .models import File


class CreateFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file',)


class ListFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file', 'upload_at', 'processed',)
