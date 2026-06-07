from django.db import models


# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/products')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name