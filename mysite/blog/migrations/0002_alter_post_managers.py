# Generated by Django 4.1.11 on 2023-09-18 21:23

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
