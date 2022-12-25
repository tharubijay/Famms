from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=500)
    image=models.ImageField(upload_to='media')
    price=models.FloatField(max_length=15)
    
    def __str__(self):
        return self.name

# class Slider(models.Model):
#     name=models.CharField(max_length=500)
#     image=models.ImageField(upload_to='media')
#     url=models.URLField(max_length=500)
#     description=models.TextField(blank=True)
#     def __str__(self):
#         return self.name

class Review(models.Model):
    name=models.CharField(max_length=300)
    image=models.ImageField(upload_to='media')
    profession=models.TextField(blank=True)
    description=models.TextField(blank=True)
    
    def __str__(self):
        return self.name


