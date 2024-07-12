from django.db import models

# Create your models here.
class DairyEntry(models.Model):
    title  = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)