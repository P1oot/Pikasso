from django.db import models
import os


class File(models.Model):
    file = models.FileField(
        verbose_name='Файл',
        upload_to='files/',
        )
    upload_at = models.DateTimeField(
        verbose_name='Время загрузки',
        auto_now_add=True,
        )
    processed = models.BooleanField(
        verbose_name='Статус загрузки',
        default=False,
        )

    def filename(self):
        return os.path.basename(self.file.name)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
