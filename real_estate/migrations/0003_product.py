# Generated by Django 5.0.4 on 2024-05-07 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0002_remove_customuser_phone_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_picture', models.ImageField(blank=True, null=True, upload_to='product_picture/')),
                ('name', models.TextField(max_length=255)),
                ('price', models.IntegerField()),
                ('area', models.TextField(max_length=255)),
            ],
        ),
    ]
