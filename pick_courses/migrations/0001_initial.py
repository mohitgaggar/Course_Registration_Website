# Generated by Django 3.2.9 on 2021-11-11 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cid', models.CharField(max_length=100)),
                ('prof_name', models.CharField(max_length=100)),
                ('prof_id', models.CharField(max_length=100)),
                ('seats_available', models.IntegerField()),
            ],
        ),
    ]
