# Generated by Django 2.2.6 on 2020-03-28 22:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000)),
                ('image', models.ImageField(blank=True, upload_to='messages/')),
                ('sent', models.DateTimeField(auto_now_add=True)),
                ('unread', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('recipient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipient', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
