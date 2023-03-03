from django.db import models

# this will be 
class CoreMenu(models.Model):
    nama= models.CharField(max_length=200, default="-")