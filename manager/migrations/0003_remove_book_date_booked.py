# Generated by Django 3.2.22 on 2023-11-28 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20231128_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='date_booked',
        ),
    ]