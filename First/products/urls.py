from django.contrib import admin
from django.urls import path,include
from products.views import( ProductListView,ProductDetailView,ProductCreateView,ProductDeleteView,ProductUpdateView,ProductView,RawCreateClass,RawUpdateClass)
app_name="products"
urlpatterns = [
   
    path("list/",ProductListView.as_view(),name="display_product_list"),
   
    #path("list/<int:lo>",ProductDetailView.as_view(),name="product_details"),
   
    path("create/",ProductCreateView.as_view(),name="create_product"),
   
    #path("delete/<int:lo>",ProductDeleteView.as_view(),name="product_delete"),
   
    path("update/<int:lo>",ProductUpdateView.as_view(),name="update_product"),
   
    #path("ftc/<int:lo>",ProductView.as_view(),name="viewa_product"),
   
    #path("ftc/",ProductView.as_view(template_name="products/product_list.html"),name="viewb_product"),
   
    #path("raw_create_class/",RawCreateClass.as_view(template_name="form.html"),name="viewc_product"),
   
    #path("raw_update_class/<int:lo>",RawUpdateClass.as_view(template_name="form.html"),name="viewd_product")

   
]