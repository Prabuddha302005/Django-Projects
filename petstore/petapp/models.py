from django.db import models

# Create your models here.
class MyPetModel(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.FloatField()


    def __str__(self):
        return f"{self.name} {self.category}"
    
    
    