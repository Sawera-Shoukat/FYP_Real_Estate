# Generated by Django 5.0.4 on 2024-05-08 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0009_alter_product_options_alter_product_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelTable(
            name='product',
            table=None,
        ),
    ]
