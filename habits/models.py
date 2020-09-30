from django.db import models
from users.models import User
from datetime import datetime, timedelta


# Create your models here.


class Habit(models.Model):
    habit_title = models.CharField(max_length=255, null=False, blank=False)
    habit_target = models.IntegerField(null=False, blank=False)
    daily_entry = models.ManyToManyField(
        DailyEntry, null=False, blank=False, on_delete=models.CASCADE)

    def habit_remaining(self):
        return int(float(self.habit_target)) - int(float(self.habit_amount))

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # When the habit was created
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Returns created_at formatted as a string in EST

    def niceCreated(self):
        nice_created = self.created_at - timedelta(hours=4)
        return nice_created.strftime("Created on %A at %I:%M %p")

    # Returns updated_at formatted as a string in EST
    def niceUpdated(self):
        nice_updated = self.updated_at - timedelta(hours=4)
        return nice_updated.strftime("Last updated on %A at %I:%M %p")

    # daily_entry = models.IntegerField(null=True, blank=True)
    # history = []

    def __str__(self):
        return f"{self.habit_title}"


class DailyEntry(models.Model):
    class Meta:
        unique_together['today_amount', 'date']
    today_amount = models.IntegerField(null=False, blank=False)
    date = models.DateField(auto_now=True, editable=True)
