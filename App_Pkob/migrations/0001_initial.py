# Generated by Django 3.2.8 on 2021-11-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('IC_no', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField(max_length=3)),
                ('Phone_no', models.IntegerField(max_length=10)),
            ],
        ),
    ]
