from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    price = models.DecimalField(
        decimal_places=2, max_digits=6, validators=[MinValueValidator(Decimal("0.01"))]
    )
