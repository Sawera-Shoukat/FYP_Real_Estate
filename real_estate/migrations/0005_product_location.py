# Generated by Django 5.0.4 on 2024-05-07 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0004_alter_product_options_alter_customuser_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.CharField(default='Unknown', max_length=255),
        ),
    ]