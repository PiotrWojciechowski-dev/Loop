# Generated by Django 2.2.6 on 2020-04-22 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0020_merge_20200422_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, choices=[('Married', 'Married'), ('Single', 'Single'), ('Its Complicated', 'Its Complicated'), ('Engaged', 'Engaged'), ('Dating', 'Dating'), ('In a relationship', 'In a relationship')], default=1, max_length=17),
        ),
    ]