# Generated by Django 3.0.2 on 2020-04-22 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='test',
            field=models.BooleanField(default=False),
        ),
    ]
