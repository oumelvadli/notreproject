from django.db import models

# Create your models here.
class Etudient(models.Model):
    id=models.CharField(max_length=6,primary_key=True)
    name=models.CharField(max_length=30)
    prenome=models.CharField(max_length=30)
    email=models.CharField(max_length=40)

    class Meta:
        db_table="tbletudient"
