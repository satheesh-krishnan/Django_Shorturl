from django.db import models


class url(models.Model):
     hexcode=models.CharField(max_length=100)
     urlcode=models.CharField(max_length=500)
 
