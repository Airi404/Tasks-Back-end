from django.db import models
from django.contrib.auth.models import User
class Person(models.Model):
    name = models.CharField(max_length=50)
    birth = models.DateField()
    slug = models.SlugField()
    picture = models.ImageField(default='def_user.png', blank=True)
    def __str__(self):
        return self.name

class Profile(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    biography = models.TextField()
    def __str__(self): 
        return f"Perfil de {self.person.name}"
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    category = models.CharField(max_length=3, choices=[('cl', 'Clothing',), ('el', 'Electronics'), ('fd', 'Food')])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, by {self.user}"

