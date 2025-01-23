from django.db import models

from core.models import PublishedModel

<<<<<<< HEAD

=======
from core.models import PublishedModel


# Категории.
>>>>>>> b5b3d533ad28d280a2ed2a7679527113b8de704b
class Category(PublishedModel):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(default=100)


<<<<<<< HEAD
=======
# Топпинги.
>>>>>>> b5b3d533ad28d280a2ed2a7679527113b8de704b
class Topping(PublishedModel):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)


<<<<<<< HEAD
class Wrapper(PublishedModel):
    title = models.CharField(
        max_length=256
    )


=======
# Обёртки.
class Wrapper(PublishedModel):
    title = models.CharField(max_length=256)


# Сорта мороженого.
>>>>>>> b5b3d533ad28d280a2ed2a7679527113b8de704b
class IceCream(PublishedModel):
    is_on_main = models.BooleanField(default=False)
    title = models.CharField(max_length=256)
    description = models.TextField()
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams'
    )
    toppings = models.ManyToManyField(Topping)