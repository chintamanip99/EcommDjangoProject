from django.db import models
from profiles.models import Profiles
from products.models import Product
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Transaction(models.Model):
	profile = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
	product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
	is_buyed=models.BooleanField(default=False,null=True,blank=True)
	def __str__(self):
		if(self.profile and self.product ):
			return ("Customer Name: "+self.profile.username+" Product Title: "+self.product.title+" id ="+str(self.id))
		else:
			return (str(self.id))