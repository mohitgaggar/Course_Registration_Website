# Generated by Django 3.2.9 on 2021-11-14 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_user_courses_taken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='courses_taken',
            field=models.TextField(null=True),
        ),
    ]
