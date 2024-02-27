from api_pikasso.celery import app
from .models import File
from django.shortcuts import get_object_or_404
from time import sleep
from pathlib import Path


@app.task
def file_processing(id):
    curent_file = get_object_or_404(File, id=id)
    suffix = Path(curent_file.filename()).suffix
    if suffix in ['.doc', '.txt', '.pdf', ]:
        print('Doing some text processing')
    elif suffix in ['.jpeg', '.img', '.png', '.jpg']:
        print('Doing some image processing')
    elif suffix in ['.py',]:
        print('Doing some Python')
    else:
        print('Doing some processing')
    sleep(3)
    curent_file.processed = True
    curent_file.save()
