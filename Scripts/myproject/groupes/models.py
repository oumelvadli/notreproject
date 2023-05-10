from django.db import models
from encadrents.models import Encadrents

# Create your models here.
class Groupes(models.Model):
    id_group=models.CharField(max_length=5,primary_key=True)
    # titre_group=models.CharField(max_length=255)
    id_encadreur=models.ForeignKey("encadrents.Encadrents", on_delete=models.PROTECT)
    






#     from django.db import models

# class Departement(models.Model):
#     nom = models.CharField(max_length=50)
#     groupes = models.ManyToManyField('Group')

# class Group(models.Model):
#     nom = models.CharField(max_length=50)
#     # Autres champs pour représenter le groupe
