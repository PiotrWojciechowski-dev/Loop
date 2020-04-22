# Generated by Django 2.2.6 on 2020-04-09 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_blocked'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='privacy_settings',
            field=models.TextField(choices=[('Open', 'Open'), ('Restricted', 'Restricted'), ('Strict', 'Strict')], default='open', max_length=10),
        ),
    ]