from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ProfileInfo, BestOffers
from phonenumber_field.modelfields import PhoneNumberField
from django import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']


class UserPhoneNumberForm(forms.ModelForm):
    class Meta:
        model = ProfileInfo
        fields = ['phone']


class AccountCompleteForm(forms.ModelForm):
    class Meta:
        model = ProfileInfo
        fields = ['address', 'address2', 'city', 'state', 'zip', 'occupation']