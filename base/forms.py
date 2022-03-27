from pyexpat import model
from django.forms import ModelForm
from .models import Professional


class ProfessionalForm(ModelForm):
    class Meta:
        model=Professional
        fields = '__all__'
        