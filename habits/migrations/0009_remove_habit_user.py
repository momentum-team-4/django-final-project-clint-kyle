# Generated by Django 3.1.1 on 2020-09-30 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0008_habit_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='user',
        ),
    ]
