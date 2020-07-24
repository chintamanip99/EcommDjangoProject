from rest_framework import serializers
from products.models import Product
from cart.models import Transaction
from profiles.models import SellerProfile

class SellerProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model=SellerProfile
		fields = ['name']

class ProductSerializer(serializers.ModelSerializer):
	seller=SellerProfileSerializer()
	class Meta:
		model = Product
		fields = ['id', 'title', 'price', 'summary', 'image','image2','image3','image4','image5','items_available','seller']

class TransactionSerializer(serializers.ModelSerializer):
	queryset=Product.objects.all()
	class Meta:
		model = Transaction
		fields = ['profile','product']