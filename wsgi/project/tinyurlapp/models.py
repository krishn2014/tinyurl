from django.db import models

# Create your models here.

class Tinyurl(models.Model):
    url = models.URLField(unique=True, blank=False)
    tiny = models.CharField(max_length=50, blank=False)