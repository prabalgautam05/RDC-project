# Generated by Django 5.0.6 on 2024-07-22 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alter_assign_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assign',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$720000$XzRSUr72c4nBiL3C1e5HHm$1YzVE6phdL/dfMplYI2Dnw6hkDcjpXhU5XWYainDbyI=', max_length=128),
        ),
    ]