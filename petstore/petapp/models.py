from django.db import models

# Create your models here.
class MyPetModel(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField(upload_to='media/', default='/static/images/fluffy_dog.webp')

    def __str__(self):
        return f"{self.name} {self.category}"
    
    
    