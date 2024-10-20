from django.db import models
from django.conf import settings
from datetime import datetime

# Create your models here.
class User(models.Model):
    id              = models.AutoField(primary_key=True)
    username        = models.CharField(max_length=150, unique=True)
    password        = models.CharField(max_length=255, null=True)
    email           = models.EmailField(max_length=255, null=True)
    role            = models.CharField(max_length=50, null=True)
    first_name      = models.CharField(max_length=100, null=True)
    last_name       = models.CharField(max_length=100, null=True)
    phone_number    = models.CharField(max_length=20, null=True)
    address         = models.TextField(null=True)
    date_joined     = models.DateTimeField(default=datetime.now)
    is_active       = models.BooleanField(default=True)

    class Meta:
        db_table = "cafe_users"
   
    def __str__(self): 
        return self.id