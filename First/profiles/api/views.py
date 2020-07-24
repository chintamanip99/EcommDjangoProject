from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes,permission_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from products.models import Product
from profiles.api.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from profiles.api.serializers import ProfilesSerializer,OTPSerializer,ProfilesAddressSerializer,ProfilesUpdateSerializer
from profiles.models import Profiles
from django.core.mail import send_mail,BadHeaderError
import random

@api_view(['POST'])
@permission_classes([])
def register_user(request):

    if request.method=='POST':
        serializer=UserSerializer(data=request.data)
        data={}
        if(serializer.is_valid()):
            user=serializer.save()
            data['username']=user.username
            data['email']=user.email
            data['password']=user.password
            token=Token.objects.get(user=user).key
            data['token']=token
        else:
            data=serializer.errors
        return Response(data)

@api_view(['POST','PUT','GET'])
@permission_classes([IsAuthenticated])
def create_profile(request):
    print(request.user)
    if request.method=='GET':
        print(request.user)
        data={}
        profile=Profiles.objects.get(user=request.user)
        data['firstname']=profile.user.first_name
        data['lastname']=profile.user.last_name
        data['balance']=str(profile.balance)
        data['age']=profile.age
        data['address']=profile.address
        data['email']=profile.user.email
        return Response(data)

    if request.method=='POST':
        print(request.user)
        serializer=ProfilesSerializer(data=request.data)
        data={}
        if(serializer.is_valid()):
            profile=serializer.save(request.user)
            data['profile_made_successfully']="Profile was successfully created"
        else:
            print(serializer.errors)
            data['error_creating_profile']="Profile was not made"
        return Response(data)

    if request.method=='PUT':
        print(request.user)
        profile=Profiles.objects.get(user=request.user)
        serializer=ProfilesUpdateSerializer(profile,data=request.data)
        data={}
        if(serializer.is_valid()):
            profile=serializer.update(request.user)
            data['profile_updated_successfully']="Profile was successfully updated"
        else:
            print(serializer.errors)
            data['error_updating_profile']="Please fill out all the fields"
        return Response(data)

########################################################AAAAAAAAAAAAADDDDDDDDDDDDDDDDDDDDRRRRRRRRRREEESSSSSSSSS
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_address(request):
    print(request.user)

    if request.method=='PUT':
        print(request.user)
        profile=Profiles.objects.get(user=request.user)
        serializer=ProfilesAddressSerializer(profile,data=request.data)
        data={}
        if(serializer.is_valid()):
            profile=serializer.update(request.user)
            data['profile_updated_successfully']="Profile was successfully updated"
            data['address']=Profiles.objects.get(user=request.user).address
        else:
            print(serializer.errors)
            data['error_updating_profile']="Please fill out all the fields"
        return Response(data)
#################################################################################################address#######

def send_email(user):
    otp=0
    try:
        otp=random.randint(100000,999998)
        if(send_mail('Email Confirmation OTP from cmpatil.pythonanywhere.com',str(otp)+"",'cmp151999@gmail.com',[user.email],fail_silently=True)>0):
            return otp
        else:
            return 0
    except BadHeaderError:
        return -1

@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def send_otp(request):
    print(request.user)
    if request.method=='GET':
        data={}
        otp=send_email(request.user)
        if(otp!=0 and otp!=-1 and len(str(otp))==6):
            data['otp_success_message']="otp sent successfully to your email address : "+request.user.email
            data['otp']=str(otp)
        if(otp==0 or otp==-1):
            data['otp_error_message']="There is some problem in connectivity try again later"
        return Response(data)

    if request.method=='POST':
        data={}
        serializer=OTPSerializer(data=request.data)
        if(serializer.is_valid()):
            if(serializer.is_verified()):
                profile=Profiles.objects.get(user=request.user)
                profile.is_email_verified=True
                profile.save()
                data['email_verification_success_message']="Email Verified Successfully"
            else:
                data['email_verification_failure_message']="Email cant be Verified"
        else:
            data['error_in_the_system']="There was some error in system, try again later"
        return Response(data)
        
        


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_profile(request):

#     if request.method=='POST':
#         print(request.data)





