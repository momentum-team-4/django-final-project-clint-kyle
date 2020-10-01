from django.forms import ModelForm, Form, CharField, ChoiceField
from .models import Habit, DailyEntry


class HabitForm(ModelForm):
    class Meta:
        model = Habit
        fields = [
            'habit_title',
            'habit_target',
        ]


class DailyEntryForm(ModelForm):
    class Meta:
        model = DailyEntry
        fields = [
            'daily_entry',
            'date',
        ]


# class HabitSearchForm(Form):
#     SEARCH = [
#         ("contains", "contains"),
#         ("exact match", "exact match"),
#     ]
#     title = CharField()
#     title_search_by = ChoiceField(choices=SEARCH)
#     body = CharField()
#     body_search_by = ChoiceField(choices=SEARCH)
