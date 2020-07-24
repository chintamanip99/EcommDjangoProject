from django.contrib import admin

# Register your models here.
from products.models import Product,Category

from profiles.models import SellerProfile


class ProductModelAdmin(admin.ModelAdmin):
	list_display=[
		'seller',
		'id',
		'title',
		'summary',
		'price',
		'new',
		'image',
		'items_available'
		]
	list_display_links=[
		
		'id'
		# 'price',
		]
	list_filter=[
		'price',
		'new'
	]
	search_fields=[
		'title',
		'price'
	]
	list_editable=[
		'price','items_available','summary','title'
	]
	class Meta:
		model=Product
	def get_queryset(self,request):
		if(request.user in [i.user for i in SellerProfile.objects.all()]):
			queryset=self.model.objects.filter(seller=request.user)
			return queryset
		if(request.user.is_superuser):
			return Product.objects.all()
admin.site.register(Category)
admin.site.register(Product,ProductModelAdmin)
