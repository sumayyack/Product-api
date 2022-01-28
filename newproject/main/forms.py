from main.models import Product
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=["product_name","price","product_image","location"]
        widgets = {
            "product_name": forms.TextInput(attrs={'class': 'form-control'}),
            "price": forms.NumberInput(attrs={'class': 'form-control'}),
            "location": forms.TextInput(attrs={'class': 'form-control'}),
        }
