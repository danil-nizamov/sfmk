# Generated by Django 4.1.3 on 2022-12-03 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='video',
            name='channel',
        ),
    ]
