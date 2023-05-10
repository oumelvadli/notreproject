from django.db import models

# Create your models here.
class Encadrents(models.Model):
    id_encad=models.CharField(max_length=5,primary_key=True)
    nom_encad=models.CharField(max_length=30)
    nom_encad=models.CharField(max_length=30)
    prenom_encad=models.CharField(max_length=30)
    email_encad=models.CharField(max_length=30)


