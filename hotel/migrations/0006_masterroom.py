# Generated by Django 3.2.22 on 2023-11-21 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_testimony'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('image', models.ImageField(upload_to='master rooms')),
            ],
        ),
    ]
