from django import forms
from . models import *
from django.contrib.auth.forms import PasswordResetForm




class CustomPasswordResetForm(PasswordResetForm):
        #Add css class
    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'pl-5 form-control'})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields  = ['photo',   ]




class DateInput(forms.DateTimeInput):
    input_type = "date"
    


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields  = ['name','quantity',  'price', 
                   'description', 'category', 'photo1', 
                   'photo2','photo3','photo4' , 'user', 'store']
        
        
    #Add css class
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['photo1'].widget.attrs.update({'class': 'form-control'})
        self.fields['photo2'].widget.attrs.update({'class': 'form-control'})
        self.fields['photo3'].widget.attrs.update({'class': 'form-control'})
        self.fields['photo4'].widget.attrs.update({'class': 'form-control'})
        self.fields['user'].widget.attrs.update({'class': 'hide'})
        self.fields['store'].widget.attrs.update({'class': 'hid'})
        