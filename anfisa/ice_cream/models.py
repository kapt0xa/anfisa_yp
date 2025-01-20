from django.db import models


# Топпинги
class Topping(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, max_length=64)
    is_published = models.BooleanField(default=True)


# Обёртки
class Wrapper(models.Model):
    title = models.CharField(max_length=256)
    is_published = models.BooleanField(default=True)


# Сорта мороженого
class IceCream(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=False)
    is_on_main = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)


# Категории
class Category(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, max_length=64)
    output_order = models.PositiveSmallIntegerField(default=100)
    is_published = models.BooleanField(default=True)
