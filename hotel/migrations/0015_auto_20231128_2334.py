# Generated by Django 3.2.22 on 2023-11-28 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0014_auto_20231128_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='check_in',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='check_out',
            field=models.DateTimeField(null=True, blank=True),
        ),

    ]
