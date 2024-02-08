from django.contrib import admin
from .models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    model = File
    list_display = ('upload_at', 'file', 'processed')
