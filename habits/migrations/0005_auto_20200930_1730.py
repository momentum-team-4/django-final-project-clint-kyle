# Generated by Django 3.1.1 on 2020-09-30 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0004_habit_daily_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='daily_entry',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
