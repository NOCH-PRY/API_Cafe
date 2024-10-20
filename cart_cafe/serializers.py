from rest_framework import serializers, fields

from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
        read_only_fields = ("id",)