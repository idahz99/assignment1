# Generated by Django 3.2.8 on 2021-11-18 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Pkob', '0006_auto_20211118_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='Timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
