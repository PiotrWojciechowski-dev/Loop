# Generated by Django 2.2.5 on 2020-03-06 13:44

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_mates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
    ]
