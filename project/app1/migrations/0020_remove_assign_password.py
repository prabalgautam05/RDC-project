# Generated by Django 5.0.6 on 2024-07-24 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_assign_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assign',
            name='password',
        ),
    ]