from django.db import models
from django.conf import settings
from datetime import datetime

# Create your models here.
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    qty = models.IntegerField()
    added_at = models.DateTimeField(default=datetime.now)
    
    class Meta:
        db_table = 'cafe_cart'
    
    def __str__(self):
        return self.id