# Generated by Django 5.0.4 on 2024-05-07 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0003_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photos/', verbose_name='Profile Photo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='area',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_picture',
            field=models.ImageField(blank=True, null=True, upload_to='product_pictures/', verbose_name='Product Picture'),
        ),
    ]
