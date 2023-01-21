from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
        category_name=models.CharField(max_length=100)
        is_active=models.BooleanField(default=True)

class Brand(models.Model):
        brand_name=models.CharField(max_length=50)


class Products(models.Model):
        name=models.CharField(max_length=250)
        owner=models.ForeignKey(User, on_delete=models.CASCADE)
        description=models.CharField(max_length=500)
        condition=(models.CharField(max_length=100, null=True))
        category=models.ForeignKey(Category,  on_delete=models.CASCADE)
        location=models.CharField(max_length=100)
        price=models.PositiveIntegerField()
        options=(
                ("for-sale","for-sale"),
                ("exchange","exchange"),
                ("sold","sold"),
                ("rent","rent")
        )
        status=models.CharField(max_length=100,choices=options, default="for-sale")
        created_date=models.DateTimeField(auto_now_add=True)
        brand=models.ForeignKey(Brand,on_delete=models.CASCADE)


class ProductImages(models.Model):
        product=models.ForeignKey(Products, on_delete=models.CASCADE)
        image=models.ImageField(upload_to='images')


class Notifications(models.Model):
        product=models.ForeignKey(Products, on_delete=models.CASCADE)
        buyer=models.ForeignKey(User,on_delete=models.CASCADE)
        description=models.CharField(max_length=150)
        options=(
                ('sent','sent'),
                ("pending","pending"),
                ("cancelled","cancelled")
        )
        status=models.CharField(max_length=100,choices=options)