# Generated by Django 5.1.2 on 2024-10-25 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_remove_sale_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='time',
            field=models.TimeField(blank=True, default='00:00:00'),
        ),
    ]
