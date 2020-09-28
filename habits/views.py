from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages import success, error
from .models import Habit
from .forms import HabitForm

# Create your views here.


def habits_list(request):
    habits = Habit.objects.all()
    return render(request, "habits/habits_list.html", {"habits": habits})


def habits_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    return render(request, "habits/habits_detail.html", {"habit": habit})


def habits_create(request):
    # habit = get_object_or_404(request, pk=pk)

    if request.method == "GET":
        form = HabitForm()

    else:
        form = HabitForm(data=request.POST)

        if form.is_valid():

            form.save()

            success(request, "Your note was created!")
            return redirect(to='habits_list')

    return render(request, "habits/habits_create.html", {"form": form})
