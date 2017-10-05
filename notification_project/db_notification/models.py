from django.db import models
from .settings import db_notification_settings as settings

# Create your models here.
class Log(models.Model):
    username      = models.CharField(max_length=150, blank=True, null=True, verbose_name='username')
    message       = models.TextField(default=None, blank=True, null=True)
    stack_trace   = models.TextField(default=None, blank=True, null=True)
    type_error    = models.TextField(default=None, blank=True, null=True)
    log_level     = models.CharField(max_length=10, blank=False, null=False, verbose_name='Log level', default=settings.LOG_LEVEL_ERROR)
    environment   = models.TextField(default=None, blank=True, null=True)
    date_time     = models.DateTimeField(auto_now_add=True, null=True)
    notes         = models.TextField(default=None, blank=True, null=True)
