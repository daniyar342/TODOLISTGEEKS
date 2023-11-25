from django.db import models

class Tasks(models.Model):
    title = models.CharField('title',max_length=80,unique=True)
    description = models.CharField('description',max_length=255)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField('Дата создания',auto_now_add=True)