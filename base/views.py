from django.shortcuts import render,redirect
from .models import  LawFaq, Professional,LegalSubTopic,LegalRight
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import ProfessionalForm,CustomerSignUpForm,EmployeeSignUpForm
from django.http import JsonResponse
from .models import *
import datetime
import json
from django.views.decorators.cache import cache_control

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = '../templates/base/register-user.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('landing')

class prof_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = '../templates/base/register-prof.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('professional-profile')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def landing(request):
    if request.method=="POST":
        cont_name=request.POST['cont_name']
        cont_email=request.POST['cont_email']
        cont_msg=request.POST['cont_msg']
        youfemail="info.youfem@gmail.com"

        finalmessage= "User Name :" + cont_name + "\n Email :" +cont_email +"\n Feedback :" + cont_msg
        print(cont_email)

        send_mail(

            cont_name,#subject
            finalmessage,#message
            cont_email,#message_email,# from email
            
            
            
            [youfemail],#to email

        )

        return render(request,'base/landing.html')
    else:
        return render(request,'base/landing.html')

def loginPage(request):

    page='login'

    if request.user.is_authenticated:
        return redirect('landing')

    if request.method=="POST":
        username=request.POST.get('username').lower()
        password=request.POST.get('password')
        usertype=request.POST.get('usertype')
       

        try:
            user=User.objects.get(username=username) 
            print(user)
        except:
            print('hi')
            messages.error(request,'User does not exist')
        print(username)
        print(password)
        
        user=authenticate(request,username=username,password=password)
        print(user)
        

        if user is not None:
            login(request,user)            

            if usertype == 'admin':
                return redirect('./admin/')
            elif usertype == 'User':
                return redirect('landing')
            elif usertype == 'Professional':
                return redirect('professional-profile')
        else:
            messages.error(request,'Username or password does not exist')

    context={'page':page}
    return render(request,'base/login.html',context)

def loginProf(request):

    page='login'

    if request.user.is_authenticated:
        return redirect('professional-profile')

    if request.method=="POST":
        peid=request.POST.get('username').lower()
        password=request.POST.get('password')
        usertype=request.POST.get('usertype')
       

        try:
            user=Professional.objects.get(peid=peid) 
            print(user)
        except:
            print('hi')
            messages.error(request,'User does not exist')
        print(peid)
        print(password)
       


        if user.password==password:
            user = user
        else:
            user =None

       
        print(user)
        

        if user is not None:
            login(request,user)            

            if usertype == 'admin':
                return redirect('./admin/')
            elif usertype == 'User':
                return redirect('landing')
            elif usertype == 'Professional':
                return redirect('professional-profile')
        else:
            messages.error(request,'Username or password does not exist')

    context={'page':page}
    return render(request,'base/login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('landing')


def registerProf(request):
    form=ProfessionalForm()

    if request.method=='POST':
        form=ProfessionalForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            prof = form.save(commit=False)
            print('hi')
            #user.username=user.username.lower()
            #prof.profile_pic = request.FILES.get('profile_pic')
            prof.save()
            print('saved')
            #login(request,user)
            return redirect('professional-profile')
        else:
            print('sad')
            messages.error(request,'An error occured during registraton')

    context={'form':form}
    return render(request,'base/register-prof.html',context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def legal(request):

    #professionals= Professional.objects.all()
    professionals= Professional.objects.filter(profession='Lawyer')
    lawyercount=Professional.objects.filter(profession='Lawyer').count()
    legalRightscount=LegalRight.objects.all().count()
    legalSubTopicscount=LegalSubTopic.objects.all().count()
    lawFaqscount=LawFaq.objects.all().count()
    #print(lawyercount)
    legalSubTopics= LegalSubTopic.objects.all()
    legalRights= LegalRight.objects.all()
    context ={'professionals':professionals,'legalSubTopics':legalSubTopics,'legalRights':legalRights,'lawyercount':lawyercount,'legalRightscount':legalRightscount,'legalSubTopicscount':legalSubTopicscount,'lawFaqscount':lawFaqscount}

    if request.method=="POST":
        message_profemail=request.POST['message-profemail']
        message_fname=request.POST['message-fname']
        message_lname=request.POST['message-lname']
        message_date=request.POST['message-date']
        message_time=request.POST['message-time']
        message_email=request.POST['message-email']
        message_phone=request.POST['message-phone']
        message=request.POST['message']

        finalmessage= "User Name :" + message_fname +" "+message_lname +"\n Message :" +message +"\n Time :" + message_time+"\n Date :"+message_date +"\n Contact Number :"+message_phone


        send_mail(

            message_fname+" " +message_lname,#subject
            finalmessage,#message
            #message_email,# from email
            message_profemail,
            
            [message_profemail],#to email

        )

        return render(request,'base/legal.html',context)

    else:
        return render(request,'base/legal.html',context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def laws(request,pk):
    legalSubTopic= LegalSubTopic.objects.get(id=pk)
    lawFaqs=LawFaq.objects.all()
    context ={'legalSubTopic':legalSubTopic,'lawFaqs':lawFaqs}
    return render(request,'base/laws.html',context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def medical(request):
    professionals= Professional.objects.filter(profession='Doctor')
    context ={'professionals':professionals}

    #return render(request,'base/mental.html', context)
    return render(request,'base/medical.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def mental(request):
    professionals= Professional.objects.filter(profession='Psychologist')
    psychoDisorder = PsychoDisorders.objects.all()
    context ={'professionals':professionals,'psychoDisorder':psychoDisorder}

    return render(request,'base/mental.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def store(request):
	
    customer=request.user.customer
    order, created=Order.objects.get_or_create(customer=customer, complete=False)
    items=order.orderitem_set.all()
    cartItems=order.get_cart_items

    products=Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'base/store.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def cart(request):
	if request.user.is_authenticated:
		customer=request.user.customer
		order, created=Order.objects.get_or_create(customer=customer, complete=False)
		items=order.orderitem_set.all()
		cartItems=order.get_cart_items
	else:
		items=[]
		order={'get_cart_total':0, 'get_cart_items':0, 'shipping':False}	
		cartItems=order['get_cart_items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'base/cart.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def checkout(request):
	if request.user.is_authenticated:
		customer=request.user.customer
		order, created=Order.objects.get_or_create(customer=customer, complete=False)
		items=order.orderitem_set.all()
		cartItems=order.get_cart_items
	else:
		items=[]
		order={'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems=order['get_cart_items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'base/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('productId:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created=Order.objects.get_or_create(customer=customer, complete=False)
	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer=request.user.customer
		order, created=Order.objects.get_or_create(customer=customer, complete=False)
		total = float(data['form']['total'])
		order.transaction_id=transaction_id

		if total == float(order.get_cart_total):
			order.complete=True
		order.save()

		if order.shipping == True:
			ShippingAddress.objects.create(
		    customer=customer,
		    order=order,
			address=data['shipping']['address'],
		    city=data['shipping']['city'],
		    state=data['shipping']['state'],
		    zipcode=data['shipping']['zipcode'],
		    )

	else:
		print('NOT LOGGED IN!')	

	return JsonResponse('Order successful!', safe=False)	
    	



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def profile(request):
    return render(request,'base/professional-profile.html')


