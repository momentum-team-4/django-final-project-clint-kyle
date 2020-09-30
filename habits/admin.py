from django.contrib import admin
from .models import Habit, DailyEntry
# Register your models here.

admin.site.register(Habit)
admin.site.register(DailyEntry)
