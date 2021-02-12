from django.db import models

class contactModel(models.Model):
 name = models.CharField(max_length=70)
 phone = models.CharField(max_length=10)
 message = models.CharField(max_length=300)

 def __str__(self):
     return self.name