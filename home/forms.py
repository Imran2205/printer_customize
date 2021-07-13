from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ProfileInfo, BestOffers, IdentityDoc, PrintFile
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


class RestrictedFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop('content_types', None)
        self.max_upload_size = kwargs.pop('max_upload_size', None)
        if not self.max_upload_size:
            self.max_upload_size = settings.MAX_UPLOAD_SIZE
        super(RestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(RestrictedFileField, self).clean(*args, **kwargs)
        try:
            if data.content_type in self.content_types:
                if data.size > self.max_upload_size:
                    raise forms.ValidationError(_('File size must be under %s. Current file size is %s.') % (filesizeformat(self.max_upload_size), filesizeformat(data.size)))
            else:
                raise forms.ValidationError(_('File type (%s) is not supported.') % data.content_type)
        except AttributeError:
            pass

        return data

class RestrictedImageField(forms.ImageField):
    def __init__(self, *args, **kwargs):
        self.max_upload_size = kwargs.pop('max_upload_size', None)
        if not self.max_upload_size:
            self.max_upload_size = settings.MAX_UPLOAD_SIZE
        super(RestrictedImageField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(RestrictedImageField, self).clean(*args, **kwargs)
        try:
            if data.size > self.max_upload_size:
                raise forms.ValidationError(_('File size must be under %s. Current file size is %s.') % (filesizeformat(self.max_upload_size), filesizeformat(data.size)))
        except AttributeError:
            pass

        return data


class IDUploadForm(forms.ModelForm):
    image = RestrictedFileField(content_types=['image/jpeg', 'application/pdf', 'image/jpg', 'image/png'])
    class Meta:
        model = IdentityDoc
        fields = ['image']

class ModelUploadForm(forms.ModelForm):
    model_file = RestrictedFileField(content_types=['model/stl', 'application/zip'])
    class Meta:
        model = PrintFile
        fields = ['model_file']