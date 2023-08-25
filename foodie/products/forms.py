
from django.contrib.gis import forms 
from django.contrib.gis.db import models 
from mapwidgets.widgets import GooglePointFieldWidget
from products.models import Products


# from django.contrib.gis.forms import ModelForm
# from django.forms import ModelForm
# This is the form for free product uploads

#Form for uploading free products
class FreeProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            "image",
            "title",
            "description",
            "category",
            "quantity",
            "pick_up_time", 
            "location", 
        ]

        widgets = {
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "pick_up_time": forms.DateInput(attrs={"class": "form-control"}),
            "location": GooglePointFieldWidget,
        }
        
#Form for uploading paid products

class PaidProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            "image",
            "title",
            "description",
            "price",
            "category",
            "quantity",
            "pick_up_time", 
            "number_of_days_listed",
            "location",
            
        ]

        widgets = {
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "pick_up_time": forms.DateInput(attrs={"class": "form-control"}),
            "number_of_days_listed": forms.NumberInput(attrs={"class": "form-control"}),
            "location": GooglePointFieldWidget(attrs={"class": "form-control"}),
        }
    
#Form to request product or service 

class RequestProductorServiceForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            "image",
            "title",
            "description",
            "category",
            "quantity",
            "pick_up_time",
            "number_of_days_listed", 
            "location", 
        ]

        widgets = {
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "pick_up_time": forms.DateInput(attrs={"class": "form-control"}),
            "number_of_days_listed": forms.NumberInput(attrs={"class": "form-control"}),
            "location": GooglePointFieldWidget(attrs={"class": "form-control"}),
        }