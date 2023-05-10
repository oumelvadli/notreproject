from django.db import models

# Create your models here.
class Sujet(models.Model):
    id_suj=models.CharField(max_length=30,primary_key=True)
    titre_suj=models.CharField(max_length=50)
    id_group=models.ForeignKey("Groupes", on_delete=models.PROTECT)
