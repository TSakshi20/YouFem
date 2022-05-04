from pyexpat import model
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Professional,User,Customer
from django.db import transaction

class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.save()
        return user


class EmployeeSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    experience = forms.CharField(required=True)
    contact= forms.CharField(required=True)
    profession =forms.CharField(required=True)
    profile_pic=forms.ImageField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        employee = Professional.objects.create(user=user)
        employee.experience=self.cleaned_data.get('experience')
        employee.profession=self.cleaned_data.get('profession')
        employee.contact=self.cleaned_data.get('contact')
        employee.profile_pic=self.cleaned_data.get('profile_pic')
        employee.save()
        return user



class ProfessionalForm(ModelForm):
    class Meta:
        model=Professional
        fields = '__all__'
        