# Generated by Django 3.2.22 on 2023-11-28 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0012_auto_20231128_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('room_type', models.CharField(max_length=50)),
                ('guests', models.CharField(max_length=50)),
            ],
        ),
    ]
