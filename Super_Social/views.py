from django.shortcuts import render
from .models import Person
from django.shortcuts import render

def SocialApp(request):
   person_list = Person.objects.all()
   return render(request, 'Super_Social/Super_Social.html', {'people': person_list})

def homepage(request):
    return render(request, 'Home.html')

def person(request, slug):
    my_person = Person.objects.get(slug = slug)
    return render(request, 'Super_Social/Person.html', {'person': my_person})


# Create your views here.
