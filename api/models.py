import random

from django.db import models
import time


class Category(models.Model):
    """
    name: Protsessor, SSD
    """
    name = models.CharField(max_length=100)


class Parameter(models.Model):
    """
    name: Chastota, xotira, model
    order - Parameter ko'rinish tartibi
    """
    name = models.CharField(max_length=50)
    order = models.IntegerField(default=0)


class CategoryParameter(models.Model):
    """
    category: SSD
    parameter: xotira, model
    """
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    parameter = models.ForeignKey(Parameter, on_delete=models.RESTRICT)


class Value(models.Model):
    """
    parameter: xotira, model
    value: 1Tb, Macbook Pro
    """
    parameter = models.ForeignKey(Parameter, on_delete=models.RESTRICT)
    value = models.CharField(max_length=100)


class Brand(models.Model):
    """
    name: Apple, Intel, Kingston
    """
    name = models.CharField(max_length=50)



class Product(models.Model):
    """
    brand: Apple
    values: (model: Macbook Pro, xotira: 512Gb)
    """
    brand = models.ForeignKey(Brand, on_delete=models.RESTRICT, default=None, null=True, blank=True)
    image = models.ImageField(upload_to=f'products/{time.time()}_{random.randint(1, 10)}/')
    # values = models.ManyToManyField(Value, default=None, null=True, blank=True)
