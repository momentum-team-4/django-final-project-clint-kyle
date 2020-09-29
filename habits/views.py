from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages import success, error
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from .models import Habit, Amount
from .forms import HabitForm

# Create your views here.

@login_required
def habits_list(request):
    habits = Habit.objects.all()
    return render(request, "habits/habits_list.html", {"habits": habits})


def habits_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    return render(request, "habits/habits_detail.html", {"habit": habit})

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


def habits_delete(request, pk):
    if request.method == 'GET':
        return render(request, 'habits/habits_delete.html')

    else:
        habit = get_object_or_404(Habit, pk=pk)
        habit.delete()
        success(request, 'Habit has been deleted!')
        return redirect(to='habits_list')
