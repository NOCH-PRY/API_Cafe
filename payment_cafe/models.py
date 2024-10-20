from django.db import models
from datetime import datetime

# Create your models here.
class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=255, null=True)
    payment_date = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'cafe_payments'

    def __str__(self):
        return self.id
