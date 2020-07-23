# Generated by Django 3.0.8 on 2020-07-23 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iknow', '0002_auto_20200723_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='issue_date',
            new_name='date_issued',
        ),
        migrations.AddField(
            model_name='publication',
            name='language',
            field=models.CharField(default='en', max_length=500),
        ),
        migrations.AddField(
            model_name='publication',
            name='video',
            field=models.CharField(default='', max_length=500),
        ),
    ]
