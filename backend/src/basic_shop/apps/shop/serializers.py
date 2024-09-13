from rest_framework import serializers
from typing import Any
from .models import Product


type Data = dict[str, Any]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "description", "price"]
