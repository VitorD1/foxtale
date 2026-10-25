from django.core.validators import MinLengthValidator
from django.db import models

from products.models import Occasion, Product
from products.validators import validate_image_size


class Article(models.Model):
    class Section(models.TextChoices):
        ABOUT = 'about', 'За мен'
        MISSION = 'mission', 'Мисия'
        HISTORY = 'history', 'История'
        IDEAS = 'ideas', 'Идеи'

    title = models.CharField(max_length=120, validators=[MinLengthValidator(3)])
    section = models.CharField(max_length=10, choices=Section.choices)
    occasion = models.ForeignKey(
        Occasion,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='articles',
    )
    text = models.TextField(validators=[MinLengthValidator(20)])
    image = models.ImageField(upload_to='articles/', blank=True, validators=[validate_image_size])
    products = models.ManyToManyField(Product, related_name='articles', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
