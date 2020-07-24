"""First URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from cart.views import send_email,show_ip_info,show_calender
from cart.api.views import get_server_url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/',include("profiles.urls")),
    path('',include("products.urls")),
    path('buy/',include("cart.urls")),
    path('emailit/',send_email),
    #REST Framework urls
    path('products_api/',include("products.api.urls","products_api")),
    path('profiles_api/',include("profiles.api.urls","profiles_api")),
    path('cart_api/',include("cart.api.urls","cart_api")),
    path('get_server_url/',get_server_url),
    path('show_ip_info/',show_ip_info),
    path('show_calender/',show_calender),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
