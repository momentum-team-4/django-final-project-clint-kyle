from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages import success, error
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from .forms import HabitForm, DailyEntryForm
from .models import *

# Create your views here.


@login_required
def habits_list(request):
    habits = Habit.objects.filter(user=request.user)
    return render(request, "habits/habits_list.html", {"habits": habits})


def habits_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    dailyentries = DailyEntry.objects.filter(habit=habit)
    remaining_today = daily_habit_remaining(habit)
    return render(request, "habits/habits_detail.html", {"habit": habit, 'dailyentries': dailyentries, 'remaining_today': remaining_today})


'''
def activity_list(request, pk):
    pass

def activity_detail(request, pk):
    pass

def activity_log(request, pk):
    pass

def activity_visualize_history(request, pk):
    activities = Activity.objects.filter(habit=pk)
    activities_js = serialize("json", activities)

    return render(request, "habits/activities/visualize.html", {"activities": activities_js})
'''


def habits_update(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    if request.method == 'GET':
        form = HabitForm(instance=habit)

    else:
        form = HabitForm(data=request.POST, instance=habit)

        if form.is_valid():
            form.save()
            success(request, 'Habit has been updated!')
            return redirect(to='habits_list')

    return render(request, 'habits/habits_update.html', {'form': form})


def habits_create(request):

    if request.method == "GET":
        form = HabitForm()

    else:
        form = HabitForm(data=request.POST)

        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user

            temp.save()

            success(request, "Your habit was created!")
            return redirect(to='habits_list')

    return render(request, "habits/habits_create.html", {"form": form})


def daily_entry(request, pk):

    if request.method == 'GET':
        form = DailyEntryForm()

    else:
        form = DailyEntryForm(data=request.POST)

        if form.is_valid():
            habit = get_object_or_404(Habit, pk=pk)
            entry = form.save(commit=False)
            entry.habit = habit
            entry.save()
            success(request, "New entry created")
            return redirect(to='habits_list')

    return render(request, 'habits/daily_entry.html', {'form': form})


def habits_delete(request, pk):
    if request.method == 'GET':
        return render(request, 'habits/habits_delete.html')

    else:
        habit = get_object_or_404(Habit, pk=pk)
        habit.delete()
        success(request, 'Habit has been deleted!')
        return redirect(to='habits_list')


# def habits_update(request, pk):
#     habit = get_object_or_404(Habit, pk=pk)

#     if request.method == 'GET':
#         form = HabitUpdate(instance=habit)

#     else:
#         form = HabitUpdate(data=request.POST, instance=habit)

#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.history.append(form.cleaned_data['daily_entry'])
#             instance.save()
#             success(request, 'Habit has been updated!')
#             return redirect(to='habits_list')

#     return render(request, 'habits/habits_update.html', {'form': form})
