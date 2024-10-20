from django.db import models
from datetime import datetime
# Create your models here.

class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    qty = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'cafe_orderItems'

    def __str__(self):
        return self.id
    