# Generated by Django 3.0.2 on 2020-04-22 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customuser_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='test',
        ),
    ]
