from django.db import models
from departements.models import Departements
from groupes.models import Groupes

# Create your models here.
class Etudient(models.Model):
    id=models.CharField(max_length=6,primary_key=True)
    name=models.CharField(max_length=30)
    prenome=models.CharField(max_length=30,default="null")
    # email=models.CharField(max_length=40)
    id_group=models.ForeignKey("groupes.Groupes", on_delete=models.PROTECT,default=0)
    id_dep=models.ForeignKey("departements.Departements", on_delete=models.PROTECT,default=0)

                           




    class Meta:
        db_table="tbletudient"
