from django.db import models
from django.urls import reverse
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

class Company(models.Model):
	name = models.CharField(max_length=20,null=False)
	description=models.TextField(max_length=200,null=False)
	address=models.CharField(max_length=100,null=False)
	authentic_certificate=models.FileField(null=True,blank=False)
	is_granted=models.BooleanField(default=False,null=False)
	def __str__(self):
		return self.name

class Profiles(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,null=True)
	address=models.CharField(max_length=200,null=False,blank=False)
	balance=models.FloatField(null=False, blank=0.0, default=0.0)
	age=models.CharField(default='25',max_length=20,blank=True,null=True)
	products_buyed=models.TextField(max_length=200,null=True,blank=True,default="hh")
	is_email_verified=models.BooleanField(default=False,null=True)
	is_regular=models.BooleanField(default=True,null=True)
	def __str__(self):
		return self.user.username
	def get_absolute_url(self):
		return reverse("display_profile_detail",kwargs={"id":self.id})

class SellerProfile(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,null=True)
	company=models.ForeignKey(Company,on_delete=models.DO_NOTHING,null=False)
	balance=models.FloatField(null=False, blank=0.0, default=0.0)
	name=models.CharField(default='abcxyz',max_length=20,null=True)
	age=models.CharField(default='25',max_length=20,blank=True,null=True)
	products_added=models.TextField(max_length=200,null=True)
	is_seller_certified_by_company=models.BooleanField(default=False,null=False)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse("display_profile_detail",kwargs={"id":self.id})

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
	if created:
		Token.objects.create(user=instance)