# Generated by Django 3.0.2 on 2020-04-15 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0016_auto_20200413_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
