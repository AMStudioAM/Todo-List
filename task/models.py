from django.db import models
from django.utils import timezone 


# Create your models here.
class Task(models.Model):
    title = models.TextField(max_length=300)
    completed = models.BooleanField(default=False) 
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title 