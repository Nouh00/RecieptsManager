from django import forms
from .models import Reciept
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Reciept
        fields = ['store_name', 'data_of_purchase', 'item_list', 'total_amount']

