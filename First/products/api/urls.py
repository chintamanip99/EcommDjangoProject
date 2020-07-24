from django.urls import path,include
from products.api.views import all_products,individual_product,get_customer_information;

app_name='products'

urlpatterns = [
	path('all_products/',all_products,name='all_products'),
	path('individual_product/<int:id>',individual_product,name='individual_product'),
	path('get_customer_information/',get_customer_information,name='get_customer_information'),
]