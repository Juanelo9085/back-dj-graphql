# Generated by Django 2.2.1 on 2019-05-09 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_serviceProfile', '0002_category_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
    ]
