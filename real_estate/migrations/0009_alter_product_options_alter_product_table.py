# Generated by Django 5.0.4 on 2024-05-07 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0008_alter_product_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.AlterModelTable(
            name='product',
            table='Products',
        ),
    ]