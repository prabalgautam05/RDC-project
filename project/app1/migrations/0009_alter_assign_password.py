# Generated by Django 5.0.6 on 2024-07-09 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_alter_assign_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assign',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$720000$hZyvUCUkeqhFyYU24vmS2U$hQmwGInyrC9MlJ42JztG49QuyJyZUXhb69xQwdKtjZs=', max_length=128),
        ),
    ]