# Generated by Django 5.0.6 on 2024-07-09 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_assign_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assign',
            name='user',
        ),
    ]
