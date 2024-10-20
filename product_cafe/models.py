from django.db import models
from django.conf import settings
from datetime import datetime

# Create your models here.
class Product(models.Model):
    id              = models.AutoField(primary_key=True)
    name            = models.CharField(max_length=255, null=True)
    description     = models.TextField(null=True)
    price           = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    category        = models.CharField(max_length=100, null=True)
    image_url       = models.URLField(max_length=255, null=True)
    is_active       = models.BooleanField(default=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cafe_products'

    def __str__(self):
        return self.id
