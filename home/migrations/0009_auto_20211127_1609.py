# Generated by Django 3.2.9 on 2021-11-27 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_user_completedcourse_user_registeredcourse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_completedcourse',
            name='course_id',
        ),
        migrations.AddField(
            model_name='user_completedcourse',
            name='completed_course_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
