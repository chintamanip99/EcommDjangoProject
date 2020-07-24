from django.urls import path,include
from cart.api.views import products_in_cart,purchased_individual_product,add_product_in_cart,purchase_a_product,delete_a_product_from_cart

app_name='cart'

urlpatterns = [
	path('products_in_cart/',products_in_cart,name='products_in_cart'),
	# path('purchased_individual_product/<int:id>',purchased_individual_product,name='purchased_individual_product'),
	path('add_product_in_cart/<int:id>',add_product_in_cart,name='add_product_in_cart'),
	path('purchase_a_product/<int:id>',purchase_a_product,name='purchase_a_product'),
	path('delete_a_product_from_cart/<int:id>',delete_a_product_from_cart,name='delete_a_product_from_cart'),
]