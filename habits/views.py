from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages import success, error
from .models import Habit
from .forms import HabitForm

# Create your views here.
def habits_list(request):
    habits = Habit.objects.all()
    return render(request, "habits/habits_list.html", {"habits": habits})