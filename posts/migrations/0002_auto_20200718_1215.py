# Generated by Django 2.2.10 on 2020-07-18 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='가제', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='recent_revised_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
