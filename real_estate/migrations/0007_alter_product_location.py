# Generated by Django 5.0.4 on 2024-05-07 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0006_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.CharField(default='', max_length=255),
        ),
    ]