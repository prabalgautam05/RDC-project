# Generated by Django 5.0.6 on 2024-07-09 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_remove_assign_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='assign',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$720000$BzylxdiALCbvMrBPbT1cAV$jdXwy/B5YAIaRDYcjWPmLT5SYIfkbLSyGBwiti3nfYY=', max_length=128),
        ),
    ]
