from django.db import models


# Категории.
class Category(models.Model):
    is_published = models.BooleanField(default=True)
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(default=100)


# Топпинги.
class Topping(models.Model):
    is_published = models.BooleanField(default=True)
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)


# Обёртки.
class Wrapper(models.Model):
    is_published = models.BooleanField(default=True)
    title = models.CharField(max_length=256)


# Сорта мороженого.
class IceCream(models.Model):
    is_published = models.BooleanField(default=True)
    is_on_main = models.BooleanField(default=False)
    title = models.CharField(max_length=256)
    description = models.TextField()
    # Создайте нужные связи между моделями:
    wrapper = models.OneToOneField(Wrapper, on_delete=models.SET_NULL,
                                   blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping, blank=False)
