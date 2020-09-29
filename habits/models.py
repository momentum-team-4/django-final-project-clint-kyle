from django.db import models
from users.models import User

# Create your models here.


class Habit(models.Model):
    habit_title = models.CharField(max_length=255, null=False, blank=False)
    habit_amount = models.IntegerField(null=False, blank=False)
    habit_target = models.CharField(max_length=255, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # daily_entry = []

    def __str__(self):
        return f"{self.habit_title}"

class Amount(models.Model):
        habit = models.ForeignKey(Habit, on_delete=models.CASCADE, null=False, blank=False)
        current_amount = models.IntegerField(null=False, blank=False)
        date = models.DateField(auto_now_add=True)