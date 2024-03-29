from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'file', 'upload_at', 'processed',)
        read_only_fields = ('id', 'upload_at', 'processed',)
