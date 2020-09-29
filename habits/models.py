from django.db import models
from users.models import User

# Create your models here.


class Habit(models.Model):
    description = models.CharField(max_length=255, null=False, blank=False)
    target_amt = models.IntegerField(null=False, blank=False)
    target_activity = models.CharField(max_length=255, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class Activity(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, null=False, blank=False)
    actual_amt = models.IntegerField(null=False, blank=False)
    date = models.DateField(auto_now_add=True)
