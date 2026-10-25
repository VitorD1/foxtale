from django.core.validators import MinValueValidator, RegexValidator
from django.db import models

from products.validators import validate_image_size


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        validators=[RegexValidator(r'^[A-Za-zА-Яа-я ]+$', 'Името може да съдържа само букви и интервали.')],
    )
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Occasion(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    occasions = models.ManyToManyField(Occasion, related_name='products', blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='products/', validators=[validate_image_size])
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(fields=['title', 'category'], name='unique_title_per_category'),
        ]

    def __str__(self):
        return self.title
