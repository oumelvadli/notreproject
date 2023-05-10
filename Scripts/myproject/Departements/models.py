from django.db import models


# Create your models here.
class Departements(models.Model):
    id_depart=models.CharField(max_length=5,primary_key=True)
    nom_dep=models.CharField(max_length=255)
    code_dep=models.CharField(max_length=10)





