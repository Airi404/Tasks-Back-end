from django.db import models

from django.db import models

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