from django import forms
from django.contrib.gis.forms.widgets import OSMWidget

from products.models import Products

# from django.contrib.gis.forms import ModelForm
# from django.forms import ModelForm
# This is the form for free product uploads


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
            "location": forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}),
        }
