from django.db import models

# Create your models here.
class Habit(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    body = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"{self.title}"