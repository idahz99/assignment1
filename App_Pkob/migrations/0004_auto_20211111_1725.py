# Generated by Django 3.2.8 on 2021-11-11 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Pkob', '0003_people_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='IC_no',
            new_name='IcNo',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='Phone_no',
            new_name='Phone',
        ),
    ]
