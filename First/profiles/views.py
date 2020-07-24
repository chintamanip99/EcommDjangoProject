from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from profiles.models import Profiles
import random
from django.core.mail import send_mail,BadHeaderError
from .forms import UserCreateForm,RawLoginForm,ProfileModelForm,ConfirmEmailForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.generic import(
	View,
	CreateView,
	ListView,
	UpdateView,
	DeleteView,
	DetailView
	)
from django.contrib import messages
# Create your views here.
def CreateUser(request):
	form=UserCreateForm()
	if request.method=='POST':
		form=UserCreateForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password1')
			user=authenticate(request,username=username,password=password)
			if user is not None:
				login(request,user)
			# messages.success(request,'Account created for the user '+user)
				messages.success(request,"  "+username+" logged in")
				return redirect("../../list/")
	context={'form':form}
	return render(request,'profiles/create_user.html',context)

def Logout(request):
	if(request.user.is_authenticated):
		logout(request)
		return redirect("/list/")
	else:
		return HttpResponse("Login First")

def Login(request):
	if not request.user.is_authenticated:
		form=RawLoginForm()
		context={'form':form}
		if request.method=='POST':
			if 2<3:
				form=RawLoginForm(request.POST)
				username=form['username'].value()
				password=form['password'].value()
				print(username,password)
				user=authenticate(request,username=username,password=password)
				if user is not None:
					login(request,user)
					messages.success(request,"  "+username+" logged in")
					return redirect("/list/")
				else:
					return HttpResponse("<h1>Wrong Credentials</h1>")
			else:
				return HttpResponse("<h1>Credentials Not valid</h1>") 
		return render(request,"profiles/create_profile.html",context)
	else:
		return HttpResponse("Already Logged in ")

class ProfileCreateView(CreateView):
	template_name="profiles/create_profile.html"
	def get(self,request,*args,**kwargs):
		if(self.request.user.is_authenticated):
			if request.user not in [i.user for i in Profiles.objects.all()]:
				form = ProfileModelForm()
				context={'form':form}
				return render(request,self.template_name,context)
			else:
				return HttpResponse("<h1>You already have a profile")
		else:
			return HttpResponse("Login First")
		
	def post(self,request,*args,**kwargs):
		if(self.request.user.is_authenticated):
			form=ProfileModelForm(request.POST)
			if form.is_valid():
				instance=form.save(commit=False)
				instance.save()
				instance.user=request.user
				instance.save()
				messages.success(request,"Profile successfully created")
				return redirect("../../list")
			else:
				return HttpResponse("wrong!!!!!!!!!!!!!!")
		else:
			return HttpResponse("Login First")
		
class ConfirmEmail(View):
	template_name="profiles/create_profile.html"
	otp=999999
	def send_email(self):
		try:
			self.otp=random.randint(100000,999998)
			print("send email: ",send_mail('Email Confirmation OTP from cmpatil.pythonanywhere.com',str(self.otp)+"",'cmp151999@gmail.com',[self.request.user.email],fail_silently=True))
		except BadHeaderError:
			print('Error')
	def get(self,request,*args,**kwargs):
		if request.user.is_authenticated:
			if(request.user in [i.user for i in Profiles.objects.all()]):
				form = ConfirmEmailForm()
				context={'form':form}
				self.send_email()
				request.session['otp']=self.otp
				return render(request,self.template_name,context)
			else:
				return HttpResponse("<h1>First Build a profile</h1>")
		else:
			return HttpResponse("<h1>Login First</h1>")
	def post(self,request,*args,**kwargs):
		if request.user.is_authenticated:
			form=ConfirmEmailForm(request.POST)
			print(str(request.session['otp'])==form['otp'].value(),str(request.session['otp']),form['otp'].value())
			if(str(request.session['otp'])==form['otp'].value()):
				instance=Profiles.objects.get(user=request.user)
				instance.is_email_verified=True
				instance.save()
				return HttpResponse("<h1>Email confirmed</h1>")
			else:
				return HttpResponse("<h1>Wrong OTP</h1>")
		else:
			return HttpResponse("<h1>Wrong OTP</h1>")

class ProfileUpdateView(UpdateView):
	template_name="profiles/create_profile.html"
	form_class=ProfileModelForm
	success_url="/list/"
	def get_object(self):
		if(self.request.user.is_authenticated):
			return get_object_or_404(Profiles,id=self.kwargs.get("lo"))
		else:
			return HttpResponse("Login First")

class ProfileDetailView(DetailView):
	queryset=Profiles.objects.all()
	def get_object(self):
		return get_object_or_404(Profiles,id=self.kwargs.get("lo"))