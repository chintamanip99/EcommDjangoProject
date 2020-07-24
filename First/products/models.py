from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
# Create your models here.

class Category(models.Model):
	name = models.CharField(default='a new category',max_length=20,null=True)
	image=models.FileField(null=True,blank=False)
	description=models.TextField(max_length=200,null=True)
	def __str__(self):
		return self.name

# class SubCategory(models.Model):
# 	name = models.CharField(default='a new sub category',max_length=20,null=True)
# 	image=models.FileField(null=True,blank=False)
# 	description=models.TextField(max_length=200,null=True)
# 	def __str__(self):
# 		return self.name

class Product(models.Model):
	seller=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,null=True)
	category=models.ForeignKey(Category,on_delete=models.DO_NOTHING,null=True)
	items_available=models.IntegerField(default=0,null=True)
	title=models.CharField(default='a new product',max_length=20,null=True)
	price=models.FloatField(null=False, blank=0.0, default=0.0)
	summary=models.TextField(max_length=200,null=True)
	new=models.BooleanField(default=True,null=True)
	image=models.FileField(null=True,blank=False)
	image2=models.FileField(null=True,blank=False)
	image3=models.FileField(null=True,blank=False)
	image4=models.FileField(null=True,blank=False)
	image5=models.FileField(null=True,blank=False)
	# slug=models.SlugField(unique=True)
	def __str__(self):
		return self.title+" seller "+self.seller.username
	def get_absolute_url(self):
		return reverse("product_details",kwargs={"id":self.id})

	class Meta:
		ordering=['title']
# def pre_save_product_receiver(sender,instance,*args,**kwargs):
# 	slug=slugify(instance.title)
# 	if Product.objects.filter(slug=slug).exists():
# 		slug="%s-%s"%(slug,instance.id)
# 		instance.slug=slug

# pre_save.connect(pre_save_product_receiver,sender=Product)