from statistics import mode
from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    

# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
#     #phone_number = models.CharField(max_length=20)
#     #location = models.CharField(max_length=20)
    

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	#name = models.CharField(max_length=200, null=True)
	#email = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Professional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    experience = models.CharField(max_length=20,null=True)
    contact = models.CharField(max_length=20,null=True)
    profession = models.CharField(max_length=20)
    profile_pic=models.ImageField(null=True,blank=True);
    password=models.CharField(max_length=30,blank=True)

    # def __str__(self):
    #     return (self.pfname+" " +self.plname)







class LegalRight(models.Model):
    #topicid=models.IntegerField(primary_key=True)
    topicname=models.CharField(max_length=50)


    def __str__(self):
        return (self.topicname)


class LegalSubTopic(models.Model):
    subtopicname=models.CharField(max_length=50)
    legaltopic=models.ForeignKey(LegalRight,on_delete=models.CASCADE)
    subtopicimage=models.ImageField(null=True,blank=True);

    def __str__(self):
        return (self.subtopicname)



class LawFaq(models.Model):
    question=models.TextField(max_length=100)
    answer=models.TextField(max_length=200)
    lawsubtopic=models.ForeignKey(LegalSubTopic,on_delete=models.CASCADE)


    def __str__(self):
        return (self.question[0:50])


    



class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	#digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def shipping(self):
		shipping = True
		# orderitems = self.orderitem_set.all()
		# for i in orderitems:
		# 	if i.product.digital == False:
		# 		shipping = True
		return shipping
	
		

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address