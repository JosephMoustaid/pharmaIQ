# Generated by Django 5.1.2 on 2024-10-25 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_alter_sale_date_alter_sale_drug_alter_sale_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archive',
            name='total_sales',
        ),
    ]
