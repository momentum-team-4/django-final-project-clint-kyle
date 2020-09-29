from django.forms import ModelForm, Form, CharField, ChoiceField
from .models import Habit


class CreateHabit(ModelForm):
    class Meta:
        model = Habit
        fields = [
            'habit_title',
            'habit_amount',
            'habit_target',
        ]

# class HabitUpdate()


# class HabitSearchForm(Form):
#     SEARCH = [
#         ("contains", "contains"),
#         ("exact match", "exact match"),
#     ]
#     title = CharField()
#     title_search_by = ChoiceField(choices=SEARCH)
#     body = CharField()
#     body_search_by = ChoiceField(choices=SEARCH)
