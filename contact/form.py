from .models import Customer 
from django import forms
class CustomerContactForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"