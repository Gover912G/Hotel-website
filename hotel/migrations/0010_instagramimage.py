# Generated by Django 3.2.22 on 2023-11-22 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_blogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='instagram images')),
            ],
        ),
    ]
