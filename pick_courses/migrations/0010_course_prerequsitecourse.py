# Generated by Django 3.2.9 on 2021-11-27 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pick_courses', '0009_auto_20211122_0632'),
    ]

    operations = [
        migrations.CreateModel(
            name='course_prerequsiteCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prerequisite_course_id', models.CharField(max_length=100, null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pick_courses.available_course')),
            ],
        ),
    ]
