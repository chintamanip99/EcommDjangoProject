from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from products.models import Product
from cart.api.serializers import ProductSerializer,TransactionSerializer
from django.contrib.auth.models import User
from cart.models import Transaction
from django.core.mail import send_mail,BadHeaderError
from profiles.models import Profiles
from profiles.models import SellerProfile

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_a_product_from_cart(request,id):
        transaction=Transaction.objects.get(id=id)
        if(transaction.is_buyed==False):
            product=transaction.product
            product.items_available+=1
            product.save()
        transaction.delete()
        return Response({'message':'Transaction deleted successfully'})

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def products_in_cart(request):
    if request.method == 'GET':
        transactions=Transaction.objects.filter(profile=request.user)
        serializer = TransactionSerializer(transactions, many=True,context={'name':request.user})
        print(request.user)
        return Response(serializer.data)

    elif request.method == 'POST':
    	seller=User.objects.get(id=1)
    	product=Product(seller=seller)
    	serializer = ProductSerializer(product,data=request.data)
    	if serializer.is_valid():
    		serializer.save()
    		return Response(serializer.data, status=status.HTTP_201_CREATED)
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def add_product_in_cart(request,id):
    data={}
    if request.method == 'GET':
        print(request.user)
        try:
            profile=Profiles.objects.get(user=request.user)
            if(profile.is_email_verified):
                product=Product.objects.get(id=id)
                if product.items_available>0:
                    if Transaction.objects.create(profile=request.user,product=product,is_buyed=False):
                        data['message']="Product was added to the cart successfully"
                        product.items_available-=1
                        product.save()
                    else:
                        data['message']="Some failure occured while adding product to he cart"
                else:
                    data['message']='The product you wish to buy is currently out of stock,we will notify you when it is in stock'
            else:
                data['message']="First Verify Email Id"
        except Profiles.DoesNotExist:
            data['message']='First make a profile to add a product in cart'
    return Response(data)

def send_email(user,id):
        try:
            if(Profiles.objects.get(user=user).is_email_verified):
                print("user=",user," transaction id=",id)
                if(send_mail('Product purchased notification from cmpatil.pythonanywhere.com',"You Have Buyed our product :"+Transaction.objects.get(id=id).product.title+" worth Rs."+str(Transaction.objects.get(id=id).product.price)+" from cmpatil.pythonanywhere.com ,Thanks For buying our product,have any suggestions for our service? email us at cmp151999@gmail.com",'cmp151999@gmail.com',[user.email],fail_silently=True)>0):
                    return 1
                else:
                    return 0
            else:
                return -1
        except BadHeaderError:
            print('Error')
            return -2

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def purchase_a_product(request,id):
    data={}
    if request.method == 'GET':
        try :
            instance=Transaction.objects.get(id=id)
            profile=instance.profile
            product=instance.product
            profile=Profiles.objects.get(user=profile)
            print(" Profile.balance"+str(profile.balance)+" Product.price"+str(product.price))
            bool1=instance.is_buyed
            if(not bool1):
                if(profile.balance>=product.price):
                    # product.items_available-=1
                    profile.balance-=product.price
                    profile.save()
                    seller=product.seller
                    seller_profile=SellerProfile.objects.get(user=seller)
                    print(seller_profile.balance,"is true",seller_profile.balance==None)
                    seller_profile.balance+=product.price
                    seller_profile.save()
                    product.save()
                    instance.is_buyed=True
                    instance.save()
                    email_status=send_email(user=request.user,id=id)
                    if(email_status==1):
                        data['email']="Email notification of product purchase sent successfully"
                    if(email_status==0):
                        data['email']="Email notification of product purchase not sent but product was successfully purchased"
                    if(email_status==-1):
                        data['email']="First confirm your email to get email notifications"
                    if(email_status==-2):
                        data['email']="Some error occured in sending mail notification"
                    data['message']="The product has been Purchased Successfully"
                else:
                    data['message']="You do not have sufficient balance to buy this product"
            if bool1:
                return Response({'message':'You have bought this product already'})
        except Transaction.DoesNotExist:
            data['message']="Id not present in transactions"
    return Response(data)

#####################Sample Code Used for Nothing##########################
@api_view(['GET', 'PUT', 'DELETE'])

@permission_classes([IsAuthenticated])
def purchased_individual_product(request, id):
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
#####################Sample Code Used for Nothing##########################

##################Get Server Url Dynamically code starts here############
@api_view(['GET'])
@permission_classes([])
def get_server_url(request):
    if request.method == 'GET':
        data={}
        data['server_url']="http://192.169.29.221:8000"
        return Response(data)
##################Get Server Url Dynamically code ends   here############

