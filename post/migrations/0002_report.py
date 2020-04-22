# Generated by Django 3.0.4 on 2020-04-22 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_reason', models.CharField(max_length=500, null=True)),
                ('report', models.CharField(choices=[('Language', 'Language'), ('Violence', 'Violence'), ('Spam', 'Spam'), ('Harassment', 'Harassment'), ('Terrorism', 'Terrorism'), ('Hate Speech', 'Hate Speech'), ('Unauthorized Sales', 'Unauthorized Sales')], default=1, max_length=18)),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='post.Post')),
            ],
        ),
    ]
