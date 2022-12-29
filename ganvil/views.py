from django.shortcuts import render
from .models import User, Item, Cart
from .serializers import UserSerializer, ItemSerializer, CartSerializer
from rest_framework import viewsets
# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
