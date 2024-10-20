from django.db import models
from datetime import datetime
# Create your models here.
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    order_date = models.DateTimeField(default=datetime.now)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    promotion_id = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cafe_orders'

    def __str__(self):
        return self.id
