# Generated by Django 3.1.6 on 2021-04-02 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputdata', '0003_auto_20210402_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='phone',
        ),
        migrations.AlterField(
            model_name='personal',
            name='phone',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
