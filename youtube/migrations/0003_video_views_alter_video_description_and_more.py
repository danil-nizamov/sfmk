# Generated by Django 4.1.3 on 2022-12-03 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0002_remove_comment_user_remove_video_channel'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='preview',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(null=True, upload_to='media/'),
        ),
    ]