# Generated by Django 3.1.1 on 2020-09-30 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_auto_20200930_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='daily_entry',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]