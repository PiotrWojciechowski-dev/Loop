# Generated by Django 3.0.2 on 2020-03-18 12:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250, null=True)),
                ('last_name', models.CharField(max_length=250, null=True)),
                ('emailAddress', models.EmailField(blank=True, max_length=250, verbose_name='Email Address')),
                ('addressline1', models.CharField(help_text='Street address, P.O box, company name, c/o', max_length=250, null=True, verbose_name='Address Line 1')),
                ('addressline2', models.CharField(blank=True, help_text='Appartment, suite, unit. building, floor, etc.', max_length=250, null=True, verbose_name='Address Line 2')),
                ('code', models.CharField(max_length=10, null=True, verbose_name='Postal code')),
                ('city', models.CharField(max_length=250, null=True, verbose_name='City')),
                ('county', models.CharField(max_length=250, null=True, verbose_name='County')),
                ('country', django_countries.fields.CountryField(max_length=2, null=True)),
                ('username', models.CharField(blank=True, max_length=250, null=True, verbose_name='username')),
                ('paid', models.BooleanField(default=False)),
                ('discount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': 'Order',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.Order')),
            ],
        ),
    ]
