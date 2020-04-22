# Generated by Django 2.2.6 on 2020-04-15 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_profile_privacy_settings'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.TextField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='workplace',
            field=models.TextField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('Married', 'Married'), ('Single', 'Single'), ('Its Complicated', 'Its Complicated'), ('Engaged', 'Engaged'), ('Dating', 'Dating'), ('In a relationship', 'In a relationship')], default=1, max_length=15),
        ),
    ]
