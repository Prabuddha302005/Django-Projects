from django.contrib import admin
from petapp import models
# Register your models here.

class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'price')

admin.site.register(models.MyPetModel, PetAdmin)
