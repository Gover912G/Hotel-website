# Generated by Django 3.2.22 on 2023-11-28 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_remove_book_date_booked'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]