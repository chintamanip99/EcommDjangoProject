from rest_framework import serializers
from products.models import Product
from profiles.models import SellerProfile
from cart.models import Transaction

class SellerProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model=SellerProfile
		fields = ['name','id']

class ProductSerializer(serializers.ModelSerializer):
	seller=SellerProfileSerializer()
	class Meta:
		model = Product
		fields = ['seller','id', 'title', 'price', 'summary', 'image']

class TransactionSerializer(serializers.ModelSerializer):
	product=ProductSerializer()
	class Meta:
		model = Transaction
		fields = ['id','profile','product','is_buyed']


