# Generated by Django 3.1.1 on 2020-09-29 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_auto_20200929_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='user',
        ),
    ]
