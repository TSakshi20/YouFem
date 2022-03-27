from django.contrib import admin

# Register your models here.

from .models import Professional,LegalRight,LegalSubTopic,LawFaq

admin.site.register(Professional)
admin.site.register(LegalRight)
admin.site.register(LegalSubTopic)
admin.site.register(LawFaq)