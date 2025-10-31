from django import forms
from .models import Product

class UploadProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category']
        widgets = {
            'category': forms.Select(attrs={
                'class': 'bg-black text-white border border-white p-2 rounded dark:bg-gray-800 dark:text-white dark:border-gray-600'
            })
        }            
