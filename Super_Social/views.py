from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UploadProduct
from .models import Person
from .models import Product
from . import forms

def SocialApp(request):
   person_list = Person.objects.all()
   return render(request, 'Super_Social.html', {'people': person_list})

def homepage(request):
    return render(request, 'Home.html')

def person(request, slug):
    my_person = Person.objects.get(slug = slug)
    return render(request, 'Person.html', {'person': my_person})

@login_required(login_url="/users/login/")
def post_new(request):
    product_list = Product.objects.all()[:20]
    if request.method == 'POST': 
        form = forms.UploadProduct(request.POST, request.FILES) 
        if form.is_valid():
            newpost = form.save(commit=False) 
            newpost.user = request.user 
            newpost.save()
            form = forms.UploadProduct()
        return render(request, 'products/list.html', { "product_list": product_list, 'form':form})
    else:
        form = forms.UploadProduct()
    return render(request, 'products/list.html', { "product_list": product_list, 'form':form})