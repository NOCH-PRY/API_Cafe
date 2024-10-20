from rest_framework import serializers, fields

from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'order_id', 'payment_method', 'payment_status', 'amount', 'transaction_id', 'payment_date')