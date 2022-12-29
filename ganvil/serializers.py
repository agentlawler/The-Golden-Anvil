from rest_framework import serializers
from .models import User, Item, Cart

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(
        many = False,
        read_only = True
    )
    item = ItemSerializer(
        many = True,
        read_only = True
    )
    class Meta:
        model = Cart
        fields = '__all__'