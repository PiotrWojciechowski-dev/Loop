# Generated by Django 3.0.4 on 2020-04-22 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_superuser',
        ),
    ]