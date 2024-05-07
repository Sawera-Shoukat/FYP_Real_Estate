from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True, verbose_name='Profile Photo')

    class Meta:
        db_table = 'custom_user'


class Product(models.Model):
    product_picture = models.ImageField(upload_to='product_pictures/', null=True, blank=True, verbose_name='Product Picture')
    name = models.CharField(max_length=255, blank=False, null=False)
    price = models.IntegerField(blank=False, null=True)
    area = models.CharField(max_length=255, blank=False, null=False)
    location = models.CharField(max_length=255, blank=False, null=False, default='')


    class Meta:
        verbose_name_plural = 'Products'
