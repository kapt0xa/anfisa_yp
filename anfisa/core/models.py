from django.db import models


class PublishedModel(models.Model):
<<<<<<< HEAD
    """Абстрактная модель. Добвляет флаг is_published."""
    is_published = models.BooleanField(default=True)

    class Meta:
        abstract = True
=======
    is_published = models.BooleanField(default=True)

    class Meta:
        abstract = True
>>>>>>> b5b3d533ad28d280a2ed2a7679527113b8de704b
