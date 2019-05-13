# Generated by Django 2.2.1 on 2019-05-11 00:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_serviceProfile', '0004_auto_20190509_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='dt_creation',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='personData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('dt_birth', models.DateField()),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer')], max_length=1)),
                ('dt_creation', models.DateField()),
                ('dt_modified', models.DateTimeField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
