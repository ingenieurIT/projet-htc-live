from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import BooleanField, CharField, DateTimeField, TextField
from django.contrib.auth.models import User


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    mobile = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.username


class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nom
    

class Ordinateur(models.Model):
    marque = models.CharField(max_length=20)
    nom = models.CharField(max_length=200)
    prix = models.FloatField(null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    description = TextField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    likesO = models.ManyToManyField(User, default=None, blank=True, related_name='likesO')
    createur = models.ForeignKey(User, on_delete=CASCADE, null=True, related_name='createur')
    maj = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-maj', '-date_creation']
    def __str__(self):
        return self.nom
    
    def likestotal(self):
        return self.likesO.count()
    
    @property
    def photoURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url
    
    @property
    def likenum(self):
        return self.likesO.all().count()


class Imagesordi(models.Model):
    ordinateur = models.ForeignKey(Ordinateur, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.ordinateur.nom
    
    


class Message(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='utilisateur')
    ordi = models.ForeignKey(Ordinateur, on_delete=models.CASCADE)
    corps = models.TextField()
    maj = models.DateTimeField(auto_now=True)
    creation = models.DateTimeField(auto_now_add=True)
    likesM = models.ManyToManyField(User, default=None, blank=True, related_name='likesM')
    
    class Meta:
        ordering = ['-maj', '-creation']
    def __str__(self):
        return self.corps
    
    
CHOIX = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Ordinateur, on_delete=models.CASCADE)
    valeur = models.CharField(choices=CHOIX, default='like', max_length=10)
    
    def __str__(self):
        return self.post
    