# Generated by Django 2.2.6 on 2020-04-27 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=256, null=True, unique=True),
        ),
    ]
