# Generated by Django 3.2.22 on 2023-11-22 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_rename_restaurant_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(default='description')),
                ('image', models.ImageField(upload_to='blogs')),
            ],
        ),
    ]
