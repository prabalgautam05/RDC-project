# Generated by Django 5.0.6 on 2024-07-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_assign_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='date_alloted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='date_resolved',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='date_started',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='assign',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$720000$WalgAL7TTs69kOmOotdwM0$wfVVcJS/MpHyNdVYwQAy6/oTMO4iEaOZsVp5BZSVDWI=', max_length=128),
        ),
    ]