# Generated by Django 3.2.9 on 2021-11-22 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pick_courses', '0008_available_course_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='available_course',
            name='days',
        ),
        migrations.RemoveField(
            model_name='available_course',
            name='description',
        ),
        migrations.RemoveField(
            model_name='available_course',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='available_course',
            name='start_time',
        ),
        migrations.AddField(
            model_name='course',
            name='days',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='start_time',
            field=models.TimeField(null=True),
        ),
    ]
