from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Product
from profiles.models import Profiles,SellerProfile
from django.core.paginator import Paginator
from .forms import ProductForm,RawProductForm,ProductUpdateForm
from django.contrib import messages
from django.views import View
from django.db.models import Q
from django.views.generic import(
	CreateView,
	ListView,
	UpdateView,
	DeleteView,
	DetailView
	)

# Create your views here.
class ProductCreateView(CreateView):
	template_name="form.html"
	def get(self,request,*args,**kwargs):
		sp=None
		try:
			sp=SellerProfile.objects.get(user=request.user)
			if(sp.is_seller_certified_by_company):
				form = ProductForm()
				context={'form':form}
				return render(request,self.template_name,context)
			else:
				return HttpResponse("<h1>You are not authenticated by company to sell the products</h1>")
		except SellerProfile.DO_NOT_EXIST:
			return HttpResponse("<h1>Seller Profile doesnt exist</h1>")
	
	def post(self,request,*args,**kwargs):
		form =ProductForm(request.POST or None,request.FILES or None)
		print("1234567")
		if form.is_valid():
			if(request.user.is_authenticated):
				instance=form.save()
				instance.seller=request.user
				instance.save()
			else:
				return HttpResponse("<h1>Not logged in</h1>")
		return redirect("/list/")
	success_url="/list/"



class ProductUpdateView(UpdateView):
    template_name="form.html"
    form_class=ProductUpdateForm
    success_url="/list/"
    queryset=Product.objects.all()
    def get_object(self):
    	if(self.request.user in [i.user for i in SellerProfile.objects.all()]):
    		return get_object_or_404(Product,id=self.kwargs.get("lo"))
    	return HttpResponse("Seller should login first")

class ProductDetailView(DetailView):
	template_name="home1.html"
	queryset=Product.objects.all()
	def get_object(self):
		return get_object_or_404(Product,id=self.kwargs.get("lo"))

class ProductDeleteView(DeleteView):
	success_url="/list/"
	l={'del':'Confirm Delete'}
	template_name="form.html"
	queryset={
	'submitbutton':'Confirm Delete'
	}
	def get_object(self):
		return get_object_or_404(Product,id=self.kwargs.get("lo"))


class ProductListView(ListView):
	template_name="products/product_list.html"
	def get_queryset(self):
		object_list=None
		try:
			search_query = self.request.GET.get('q')
			search_query=search_query.strip()
			object_list=Product.objects.filter(Q(title__icontains=search_query) |  Q(summary__contains=search_query))
			
		except Exception as e:
			object_list=Product.objects.all()
			print(e)
		queryset={'is_seller':False,'is_email_verified':False,'is_customer':True,'has_profile':False,'profile_id':None}
		if(self.request.user in [i.user for i in SellerProfile.objects.all()] and self.request.user.is_authenticated):
			messages.success(self.request,'List of Products you have added till now :')
			queryset={'is_seller':True,'is_customer':False,'object_list':object_list.filter(seller=self.request.user).order_by('id')}
		else:
			messages.success(self.request,'We Have A Range of Products listed below')
			if self.request.user.is_authenticated:
				has_profile=self.request.user in [i.user for i in Profiles.objects.all()]
				profile_id=0
				if(has_profile):
					profile_id=Profiles.objects.get(user=self.request.user).id
					queryset.update({'is_email_verified':Profiles.objects.get(user=self.request.user).is_email_verified,'profile_id':profile_id,'has_profile':has_profile})
					print(queryset)
			object_list_list=object_list
			paginator = Paginator(object_list_list, 10)
			page_number=self.request.GET.get('page')
			page_obj = paginator.get_page(page_number)
			# print("pgno",page_obj.page_number)
			has_next_page=False
			has_previous_page=False
			if(page_number==1):
				has_previous_page=False
				has_next_page=True
			queryset.update({'object_list':page_obj})
		return queryset

class RawCreateClass(View):
	template_name="products/form.html"
	def get(self,request,*args,**kwargs):
		print("yuyu")
		form = ProductForm()
		context={'form':form}
		return render(request,self.template_name,context)
	def post(self,request,*args,**kwargs):
		form =ProductForm(request.POST or None,request.FILES or None)
		if form.is_valid():
			print(form.save())
			form = ProductForm()
		context={'form':form}
		return render(request,self.template_name,context)

###########################################################
class RawUpdateClass(View):
	template_name="products/form.html"
	def get_object(self):
		if self.kwargs.get('lo') is not None:
			obj=get_object_or_404(Product,id=self.kwargs.get('lo'))
		return obj
	def get(self,request,*args,**kwargs):
		context={}
		print("yuyu")
		obj=self.get_object()
		form = ProductForm(instance=obj)
		context['form']=form
		context['object']=obj
		return render(request,self.template_name,context)
	def post(self,request,*args,**kwargs):
		context={}
		obj=self.get_object()
		if obj is not None:
			form =ProductForm(request.POST or None,request.FILES or None,instance=obj)
			print("1234567")
			if form.is_valid():
				print("Valid ahe re bhauuu!!")
				print(form.save())
			object_list=Product.objects.all()
			context['object_list']=object_list
		return render(request,"products/product_list.html",context)
###########################################################

class ProductView(View):
	template_name="home1.html"
	def get(self,req,lo=None):
		print('req',req.user)
		if(lo is not None):
			obj=get_object_or_404(Product,id=lo)
		else:
			obj=Product.objects.all()
		mydict={
		# 'products':product,
		'object_list':obj,
		'dict1':{'message':"how's the josh!!!!","reply":"high sir!!!!"},
	 	'list1':[1,2,3,4]
		}
		return render(req,self.template_name,mydict)	

