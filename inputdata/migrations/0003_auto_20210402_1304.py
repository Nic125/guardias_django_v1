# Generated by Django 3.1.6 on 2021-04-02 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inputdata', '0002_auto_20210402_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='personal_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inputdata.personal'),
        ),
    ]
