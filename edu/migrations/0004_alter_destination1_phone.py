# Generated by Django 4.0.1 on 2022-04-06 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0003_destination1_delete_destination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination1',
            name='phone',
            field=models.IntegerField(verbose_name=20),
        ),
    ]
