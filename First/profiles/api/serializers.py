from rest_framework import serializers
from django.contrib.auth.models import User
from profiles.models import Profiles


			
class UserSerializer(serializers.ModelSerializer):
	password2=serializers.CharField(write_only=True)
	email=serializers.CharField(write_only=True)
	class Meta:
		model=User
		fields=['username','email','password','password2']
		extra_kwargs={
		'password':{'write_only':True}
		}

	def save(self):
		username=self.validated_data['username']
		password=self.validated_data['password']
		password2=self.validated_data['password2']
		email=self.validated_data['email']
		if password!=password2:
			raise serializers.ValidationError({'password':'Passwords doesnt match'})
		user=User.objects.create_user(
			email=email,
			username=username,
			password=password
			)
		user.save()
		return user

class ProfilesAddressSerializer(serializers.ModelSerializer):
	address=serializers.CharField(write_only=True)
	class Meta:
		model=Profiles
		fields=['address']

	def update(self,user1):
		user=user1
		print(user.username)
		profile=Profiles.objects.get(user=user)
		profile.address=self.validated_data['address']
		profile.save()
		return profile

class ProfilesSerializer(serializers.ModelSerializer):
	firstname=serializers.CharField(write_only=True)
	lastname=serializers.CharField(write_only=True)
	balance=serializers.CharField(write_only=True)
	class Meta:
		model=Profiles
		fields=['age','firstname','lastname','balance','address']

	def save(self,user1):
		user=user1
		print(user.username)
		balance=float(self.validated_data['balance'])
		print(balance+1)
		age=self.validated_data['age']
		user.first_name=self.validated_data['firstname']
		user.last_name=self.validated_data['lastname']
		user.save()
		profile=Profiles.objects.create(
				user=user,
				age=age,
				balance=balance,
				address=self.validated_data['address']
			)
		profile.save()
		return profile

class ProfilesUpdateSerializer(serializers.ModelSerializer):
	firstname=serializers.CharField(write_only=True)
	lastname=serializers.CharField(write_only=True)
	balance=serializers.CharField(write_only=True)
	email=serializers.CharField(write_only=True)
	class Meta:
		model=Profiles
		fields=['age','firstname','lastname','balance','address','email']


	def update(self,user1):
		user=user1
		print(user.username)
		balance=float(self.validated_data['balance'])
		print(balance+1)
		age=self.validated_data['age']
		user.first_name=self.validated_data['firstname']
		user.last_name=self.validated_data['lastname']
		profile=Profiles.objects.get(user=user)
		profile.user=user
		profile.age=age
		if(user.email != self.validated_data['email']):
			profile.is_email_verified=False
		user.email=self.validated_data['email']
		profile.balance=float(balance)
		profile.address=self.validated_data['address']
		user.save()
		profile.save()
		return profile

class OTPSerializer(serializers.ModelSerializer):
	otp1=serializers.CharField(write_only=True)
	otp2=serializers.CharField(write_only=True)
	class Meta:
		model=User
		fields=['otp1','otp2']
	def is_verified(self):
		if(self.validated_data['otp1']==self.validated_data['otp2']):
			return True
		else:
			return False
	

# class LoginSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model=User
# 		fields=['username','password']
		

	