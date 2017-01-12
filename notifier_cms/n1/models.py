from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Notification(models.Model):
    display_date = models.DateTimeField()
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title