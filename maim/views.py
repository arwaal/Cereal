from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

# Create your views here.

from django.views.generic import View 
from maim.models import Cereal, Manufacturer, NutriFact
from maim.forms import CerealSearch, CreateCereal
from maim.forms import UserSignup, UserSignin




def cereal_list(request):

	manufacturers = Manufacturer.objects.all().order_by('name')

	cereal_string = ""

	for manufacturer in manufacturers:
		cereal_string += " <h4>%s </h4></br>" % manufacturer
		for cereal in manufacturer.cereal_set.all():
			cereal_string += "%s </br>" % cereal.name


	return HttpResponse(cereal_string)



def get_cereal_search(request):

	print request.GET
	# cereal = request.GET['cereal']
	cereal = request.GET.get('cereal', 'None')

	cereals = Cereal.objects.filter(name__istartswith=cereal)

	cereal_string ="""
	<form action='/get_cereal_search/' method='GET'>

	Cereal:
	</br>
	<input type="text" name="cereal">

	</br>
	<input type="submit" value="Submit">
	</form>
	"""

	for cereal in cereals:
		cereal_string +="%s</br>" % cereal.name
		# for nutri_list in 

	return HttpResponse(cereal_string)


def cereal_search (request, cereal):

	cereals = Cereal.objects.filter(name__istartswith=cereal)
	cereal_string =""
	for cereal in cereals:
			cereal_string+= "<b>Cereal:</b></br>%s, Manufacturer:%s </br>" % (cereal.name,cereal.manufacturer)

	return HttpResponse(cereal_string)


def get_manufacturer_search(request):

	print request.GET
	manufacturer=request.GET.get('manufacturer','None')


	manufacturers = Manufacturer.objects.filter(name__istartswith=manufacturer)
	manu_string = """

	<form action='/get_manufacturer_search/' method='GET'>

	Manufacturer:
	</br>
	<input type="text" name="manufacturer">

	</br>
	<input type="submit" value="Submit">
	</form>
	"""

	for manufacturer in manufacturers:
		manu_string += " %s" % (manufacturer.name)

	return HttpResponse(manu_string)


def manu_list(request):
	manu = Manufacturer.objects.all()
	manu_string = ""

	for manufacturer in manu:
		manu_string += "%s </br>" % manufacturer

	return HttpResponse(manu_string)


def manu_search(request, manufacturer):
	manu = Manufacturer.objects.filter(name__istartswith=manufacturer)
	manu_string = ""
	for manufacturer in manu:
		manu_string +="<b>Manufacturer:</b></br>%s " % (manufacturer.name)

	return HttpResponse(manu_string)
 

def nutrinfo(request):
	# cereals = Cereal.objects.filter(name__istartswith='h')
	# context ={}
	# context['cereals_with_a'] = cereals

	# render(request, 'cereal_list.html')
	# cereals = Cereal.objects.all()

	# Cereals = Cereal.objects.all()

	nutrifacts = NutriFact.objects.all()
	context = {}
	context[ 'nutrifacts' ] = nutrifacts
	return render(request, 'cereal_list.html', context)

	# cereals = Cereal.objects.all()
	# context ={}
	# context['cereals'] = cereals
	# return render(request, 'cereal_list.html', context)





def cereal_list2(request):
	manufacturers = Manufacturer.objects.all().order_by('name')
	print manufacturers
	context ={}
	manufacturer_cereal = {}
	for manufacturer in manufacturers:
		cereals= manufacturer.cereal_set.filter(name__icontains="a").order_by('name')
		manufacturer.name = {manufacturer.name: cereals}
		manufacturer_cereal.update(manufacturer.name)
	context['manufacturer_cereal'] = manufacturer_cereal
	
	# return render(request, 'cereal_list2.html', context)
	return render_to_response('cereal_list2.html', context, context_instance=RequestContext(request))

def cereal_detail(request, pk):
	context ={}
	cereal = Cereal.objects.get(pk=pk)
	context ['cereal'] = cereal
	return render_to_response('cereal_detail.html', context, context_instance=RequestContext(request))



def form_view(request):

	context ={}

	get = request.GET
	post = request.POST

	context['get']= get
	context['post']= post

	if request.method == "POST":
		cereal = request.POST.get('cereal', None)

		cereals = Cereal.objects.filter(name__istartswith=cereal)

		context ['cereals']= cereals

	elif request.method == "GET":
		context ['method']='The method was GET'


	return render_to_response('form_view.html', context, context_instance=RequestContext(request))



def form_view2(request):

	context ={}

	get = request.GET
	post = request.POST

	context['get']= get
	context['post']= post

	form = CerealSearch()
	context['form'] = form


	if request.method == "POST":
		form = CerealSearch(request.POST)

		if form.is_valid():
			cereal = form.cleaned_data['name']

			cereals = Cereal.objects.filter(name__istartswith=cereal)

			context ['cereals']= cereals
			context ['valid'] = "The Form Was Valid"
		else:
			context['valid'] = form.errors

	elif request.method == "GET":
		context ['method']='The method was GET'


	return render_to_response('form_view2.html', context, context_instance=RequestContext(request))

def cereal_create(request):
	context = {}

	form = CreateCereal()
	context['form'] = form

	if request.method =='POST':
		form = CreateCereal(request.POST)

		if form.is_valid():
			form.save()

			context['valid'] = "Cereal Saved"

	elif request.method == 'GET':
		context['valid'] = form.errors


	return render_to_response('cereal_create.html', context, context_instance=RequestContext(request))

def signup(request):

	context ={}
	form = UserSignup()
	context['form'] = form

	if request.method == 'POST':
		form = UserSignup(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			password = form.cleaned_data
			try:
				User.objects.create_user(name,email,password)
				context['valid'] = "Thank You For Signing Up"
				auth_user = authenticate(username=name, password=password)
				login(request, auth_user)
				return HttpResponseRedirect('/nutrinfo/')
			except IntegrityError, e:
				context['valid'] = "A User With That Name Already Exsists"
		else:
			context['valid'] = form.errors
	if request.method =='GET':
		context ['valid'] = "Please Sign Up!"


	# User.objects.create_user('Bob','bob@bobnet.bob','iamthebob')

	return render_to_response('signup.html', context, context_instance=RequestContext(request))


def home(request):

	# context = {}

	# manu = Manufacturer.objects.all().order_by('name')

	# context ['manu'] = manu

	return render_to_response('home.html', {},context_instance=RequestContext(request))


def signin(request):
	context={}
	context['form'] = UserSignin()
	username = request.POST.get('username', None)
	password = request.POST.get('password', None)

	auth_user = authenticate(username=username,password=password)

	if auth_user is not None:
		if auth_user.is_active:
			login(request, auth_user)
			context['valid'] = "Login Successful"

			return HttpResponseRedirect('/home/')

		else:
			context['valid'] = "Invalid User"
	else:
		context['valid'] = "Please enter a User Name"

	return render_to_response('signin.html',context, context_instance=RequestContext(request))


def logout_view(request):

	logout(request)

	return HttpResponseRedirect('/signin/')


	

 









	
