# Generated by Django 3.0.8 on 2020-07-23 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iknow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]