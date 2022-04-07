# Generated by Django 4.0.1 on 2022-04-06 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0002_destination_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Destination',
        ),
    ]