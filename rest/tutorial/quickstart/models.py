from django.db import models

# Create your models here.


class Cars(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField(max_length=255)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    rego = models.CharField(max_length=255)

class Smartphon(Cars):
    pass
  
