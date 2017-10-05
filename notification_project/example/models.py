from django.db import models


# Create your models here.
class Example(models.Model):
    first_name     = models.CharField(max_length=150, blank=True, null=True)
    last_name      = models.CharField(max_length=150, blank=True, null=True)
    message        = models.TextField(default=None, blank=True, null=True)
