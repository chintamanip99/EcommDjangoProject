from django.shortcuts import render
from django.core.mail import send_mail,BadHeaderError
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect


from django.template.loader import render_to_string


from .models import Transaction
from profiles.models import Profiles
from products.models import Product
from django.contrib.auth.decorators import login_required
from .forms import TransactionRawForm,TransactionRawForm1
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import(
	CreateView,
	ListView,
	UpdateView,
	DeleteView,
	DetailView
	)
# Create your views here.

class TransactionCreateView(CreateView):
	template_name="cart/form.html"
	form_class=TransactionRawForm
	success_url="/buy/list"



counter=0
def send_email(request):
	global counter
	for i in range(1):
		try:
			print("send email: ",send_mail('Deejango Abyassssss basss kaar',"rr",'cmp151999@gmail.com',['cmp151999@gmail.com'],html_message=render_to_string('mail_template.html',{'context':Product.objects.get(id=10).image.url}),fail_silently=True))
			counter+=1
		except BadHeaderError:
			return HttpResponse("<h1>avghad ahe</h1>")
	return HttpResponse("<h1>YUPPP</h1>")

class TransactionListView(ListView):
	def get_queryset(self):
		if(self.request.user.is_authenticated):
			queryset=Transaction.objects.filter(profile=self.request.user)
		return queryset
	
class TransactionDetailView(DetailView):
	queryset=Transaction.objects.all()
	def get_object(self):
		return get_object_or_404(Transaction,id=self.kwargs.get("lo"))

class TransactionDeleteView(DeleteView):
	template_name="cart/form.html"
	form_class=TransactionRawForm
	success_url="/buy/list"
	def get_object(self):
		if(self.request.user.is_authenticated):
			obj=get_object_or_404(Transaction,id=self.kwargs.get("lo"))
			obj1=obj.product
			obj1.items_available+=1
			obj1.save()
			return obj
		else:
			return get_object_or_404(Transaction,id=-9999)

class TransactionDeleteWithoutChangeView(DeleteView):
	template_name="cart/form.html"
	form_class=TransactionRawForm
	success_url="/buy/list"
	def get_object(self):
		if(self.request.user.is_authenticated):
			obj=get_object_or_404(Transaction,id=self.kwargs.get("lo"))
			return obj
		else:
			return get_object_or_404(Transaction,id=-9999)

class TransactionUpdateView(UpdateView):
    template_name="cart/form2.html"
    form_class=TransactionRawForm1
    success_url="/buy/list"
    # queryset=Transaction.objects.all()
    def send_email(self):
    	try:
    		if(Profiles.objects.get(user=Transaction.objects.get(id=self.kwargs.get('lo')).profile).is_email_verified):
    			if(send_mail('Product purchased notification from cmpatil.pythonanywhere.com',"You Have Buyed our product :"+Transaction.objects.get(id=self.kwargs.get('lo')).product.title+" worth Rs."+str(Transaction.objects.get(id=self.kwargs.get('lo')).product.price)+" from cmpatil.pythonanywhere.com ,Thanks For buying our product,have any suggestions for our service? email us at cmp151999@gmail.com",'cmp151999@gmail.com',[self.request.user.email],fail_silently=True)>0):
    				return True
    			else:
    				return False
    		return HttpResponse("Mail is not confirmed")
    	except BadHeaderError:
    		print('Error')
    		return False
    		
    def get_object(self):
    	if(self.request.user.is_authenticated):
    		print("authentttttttttttttttttttttttttttttticatedddddddddddddddddddddddddddddddd")
    		if(not Transaction.objects.get(id=self.kwargs.get('lo')).is_buyed and Profiles.objects.get(user=Transaction.objects.get(id=self.kwargs.get('lo')).profile).is_email_verified):
    			obj=get_object_or_404(Transaction,id=self.kwargs.get("lo"))
    			print("Object returneddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
    			return obj
    		else:
    			print("Object not returneddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
    			return get_object_or_404(Transaction,id=-999)
    	else:
    		print("not authentttttttttttttttttttttttttttttticatedddddddddddddddddddddddddddddddd")
    		return get_object_or_404(Transaction,id=-999)

    def post(self,request,*args,**kwargs):
    	if(request.user.is_authenticated):
    		form=TransactionRawForm1(request.POST)
    		instance1=Transaction.objects.get(id=self.kwargs.get("lo"))
    		instance1.is_buyed=form['is_buyed'].value()
    		instance1.save()
    		if(form['is_buyed'].value()==True):
    			if(not self.send_email()):
    				return HttpResponse("Some thing went wrong while sending mail,but product order is placed successfully")
    		print("lllllllllllllllll00000000pppppppppppp")
    		return redirect("../../buy/list")
    	else:
    		return HttpResponse("Login First")


    		

# def buyit(request,lo):
# 	o=Product.objects.get(id=lo)
# 	o.save()
# 	# o1=User.objects.get(id=request.user.id)
# 	# o1.save()
# 	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@save?"+str(o.title))
# 	# o1=request.user
# 	# o1.save()
# 	obj=Transaction(product=o)
# 	obj.save()
# 	return render("../../products/list")
# 	# else:
# 	# 	return HttpResponse("<h1>wrong</h1>") 
class CreateTransaction(View):
	# @login_required(login_url="../../products/list")
	def get(self,request,*args,**kwargs):
		context={}
		if request.user.is_authenticated:
			if(request.user in [i.user for i in Profiles.objects.all()]):
				if(Product.objects.get(id=self.kwargs.get('lo')).items_available>0):
					form=TransactionRawForm()
					context['form']=form
					return render(request,"cart/form.html",context)
				else:
					return HttpResponse("Out Of Stock")
			else:
				return HttpResponse("<h1>First Make a Profile")
		else:
			return HttpResponse("<h1> Login first</h1>")

	def post(self,request,*args,**kwargs):
		form=TransactionRawForm(request.POST)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.save()
			instance.profile=request.user
			prod=Product.objects.get(id=self.kwargs.get('lo'))
			if(prod.items_available>0):
				prod.items_available-=1
				prod.save()
				instance.product=prod
				instance.save()
				messages.success(request,"Product was successfully placed in cart")
				print("hhuu")
				return redirect("../../list/")
			else:
				return  HttpResponse("Out of Stock")
		else:
			return HttpResponse("wrong!!!!!!!!!!!!!!")


###############################The following code is for the javascript application that shows ip address information############################################################################
def show_ip_info(request):
    return render(request,"cart/js_app.html")

def show_calender(request):
    return render(request,"cart/js_calender.html")


##############################End of js application##############################################################################################################################################