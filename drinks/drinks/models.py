from django.db import models
from tables import Description
 
class Drink(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.name+'__'+self.description