# Generated by Django 3.0.2 on 2020-04-09 16:14

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20200404_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_file',
            field=models.FileField(blank=True, upload_to=post.models.Post.upload_path),
        ),
    ]
