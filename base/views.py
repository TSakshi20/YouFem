from django.shortcuts import render,redirect
from .models import  LawFaq, Professional,LegalSubTopic,LegalRight
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfessionalForm
# Create your views here.

# def home(request):
#     return render(request,'base/home.html')


def landing(request):
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
            elif usertype == 'user':
                return redirect('landing')
            elif usertype == 'professional':
                return redirect('landing')
        else:
            messages.error(request,'Username or password does not exist')

    context={'page':page}
    return render(request,'base/login.html',context)



def loginProf(request):

    page='login'

    if request.user.is_authenticated:
        return redirect('landing')

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

            
        #user=authenticate(request,peid=peid,password=password)
        print(user)
        

        if user is not None:
            login(request,user)            

            if usertype == 'admin':
                return redirect('./admin/')
            elif usertype == 'user':
                return redirect('landing')
            elif usertype == 'professional':
                return redirect('landing')
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
            return redirect('landing')
        else:
            print('sad')
            messages.error(request,'An error occured during registraton')

    context={'form':form}
    return render(request,'base/register-prof.html',context)


    # if request.method=='POST':
    #     first_name=request.POST.get('first_name')
    #     last_name=request.POST.get('last_name')
    #     email=request.POST.get('email')
    #     experience=request.POST.get('experience')
    #     profession=request.POST.get('profession')
    #     contact=request.POST.get('profession')
    #     profile_pic=request.POST.get('f')
    #     password1=request.POST.get('password1')
    #     password2=request.POST.get('password2')
        
    #     if password1 == password2:
    #         user=Professional.objects.create_user(password=password1,experience=experience,profession=profession,contact=contact,email=email,profile_pic=profile_pic,first_name=first_name,last_name=last_name)
    #         user.save()
    #         print("user created");

    #     else:
    #         print('password not matching')
    #         #messages.error(request,'Passwords dont match !!')
    #     return redirect('landing')
        
        
    # return render(request,'base/register-prof.html')

def registerUser(request):
    


    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        
        if password1 == password2:
            user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
            user.save()
            print("user created");

        else:
            print('password not matching')
            #messages.error(request,'Passwords dont match !!')
        return redirect('landing')
        
        

    return render(request,'base/register-user.html')



def legal(request):

    professionals= Professional.objects.all()
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



def laws(request,pk):
    legalSubTopic= LegalSubTopic.objects.get(id=pk)
    lawFaqs=LawFaq.objects.all()
    context ={'legalSubTopic':legalSubTopic,'lawFaqs':lawFaqs}
    return render(request,'base/laws.html',context)

def medical(request):
    return render(request,'base/medical.html')


def mental(request):
    return render(request,'base/mental.html')


# def legal(request):
#     return HttpResponse('Legal')
