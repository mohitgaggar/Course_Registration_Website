# Generated by Django 3.2.9 on 2021-11-19 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_myuser_registered_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='registered_course',
            new_name='registered_courses',
        ),
    ]
