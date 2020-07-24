from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from products.models import Product
from products.api.serializers import ProductSerializer,TransactionSerializer
from django.contrib.auth.models import User
from cart.models import Transaction
from profiles.models import SellerProfile,Profiles

@api_view(['GET', 'POST'])
@permission_classes([])
def all_products(request):
    

    # if request.method == 'GET' and not request.user.is_anonymous:
    # 	try:
    # 		seller=SellerProfile.objects.get(user=request.user)
    # 		print(request.user)
    # 		products = Product.objects.filter(seller=request.user)
    # 		serializer = ProductSerializer(products, many=True)
    # 		return Response(serializer.data)
    # 	except SellerProfile.DoesNotExist:
    # 		data={}
    # 		data['seller_doesnt_exist']="Seller doesnt exist"
    # 		print(request.user)
    # 		products = Product.objects.all()
    # 		serializer = ProductSerializer(products, many=True)
    # 		return Response(serializer.data)

    if request.method == 'GET':
    	data={}
    	print(request.user)
    	products = Product.objects.all()
    	serializer = ProductSerializer(products, many=True)
    	return Response(serializer.data)
    		


    elif request.method == 'POST':
    	seller=User.objects.get(id=1)
    	product=Product(seller=seller)
    	serializer = ProductSerializer(product,data=request.data)
    	if serializer.is_valid():
    		serializer.save()
    		return Response(serializer.data, status=status.HTTP_201_CREATED)
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
@permission_classes([])
def get_customer_information(request):
	print(request.data)
	try:
		profile=Profiles.objects.get(user=request.user)
		return Response({'address':profile.address,'has_profile':True,'profile_id':profile.id,'is_email_verified':profile.is_email_verified})
	except Profiles.DoesNotExist:
		return Response({'has_profile':False})


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def individual_product(request, id):
	if SellerProfile.objects.get(user=request.user) is not None:
		try:
			product = Product.objects.get(id=id)
		except Product.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		if request.method == 'GET':
			serializer = ProductSerializer(product)
			return Response(serializer.data)

		elif request.method == 'PUT':
			serializer = ProductSerializer(product, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		elif request.method == 'DELETE':
			product.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
	else:
		return Response({'Authorization Error':'You have to be a seller to add a product to sell'})

