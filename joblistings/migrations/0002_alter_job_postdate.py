# Generated by Django 4.1.13 on 2024-01-07 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joblistings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='postdate',
            field=models.CharField(max_length=100),
        ),
    ]
