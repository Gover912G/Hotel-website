# Generated by Django 3.2.22 on 2023-11-21 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='background1',
            field=models.ImageField(default='image', upload_to='background'),
        ),
        migrations.AddField(
            model_name='about',
            name='background2',
            field=models.ImageField(default='image', upload_to='background'),
        ),
    ]
