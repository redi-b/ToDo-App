from django.db import models

# Create your models here.
class Todo(models.Model):

    added_date = models.DateTimeField('Date Added', auto_now=True)
    text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
