# Generated by Django 2.2.1 on 2019-05-11 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_serviceProfile', '0005_auto_20190510_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persondata',
            name='dt_creation',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='persondata',
            name='dt_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='persondata',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]