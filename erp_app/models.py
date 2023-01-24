from django.db import models

# Create your models here.

class Product(models.Model):
    
    product_id = models.CharField(max_length=50, default="")
    product_name = models.CharField(max_length=50, default="")
    product_category = models.CharField(max_length=30, default="")




class User(models.Model):
    
    username = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50, default="")
    # product_category = models.CharField(max_length=30, default="")