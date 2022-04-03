from django.contrib import admin

# Register your models here.

#from .models import Professional,LegalRight,LegalSubTopic,LawFaq
from .models import *

admin.site.register(Professional)
admin.site.register(LegalRight)
admin.site.register(LegalSubTopic)
admin.site.register(LawFaq)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)