from django.db import models
from django.conf import settings
from datetime import datetime


# Create your models here.
class Promotion(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    discount_type = models.CharField(max_length=50)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'cafe_promotions'
    
    def __str__(self):
        return self.id
