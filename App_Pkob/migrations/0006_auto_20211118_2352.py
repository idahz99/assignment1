# Generated by Django 3.2.8 on 2021-11-18 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Pkob', '0005_remove_people_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='Phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='people',
            name='Timestamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]
