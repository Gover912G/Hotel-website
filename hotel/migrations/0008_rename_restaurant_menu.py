# Generated by Django 3.2.22 on 2023-11-22 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_restaurant'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restaurant',
            new_name='Menu',
        ),
    ]