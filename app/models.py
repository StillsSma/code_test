from django.db import models

# Create your models here.

class Entry(models.Model):
    value = models.CharField(max_length=40)
