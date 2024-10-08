# Generated by Django 5.1.1 on 2024-09-13 12:32

import django_jsonform.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('options', django_jsonform.models.fields.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', django_jsonform.models.fields.JSONField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
