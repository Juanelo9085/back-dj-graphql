from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
  category = models.CharField(max_length=50)
  dt_creation = models.DateField()
  dt_modified = models.DateTimeField()

  def __str__(self):
    return self.name

class personData(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  dt_birth = models.DateField()
  phone = models.CharField(max_length=15)
  GENDER= (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    )
  gender = models.CharField(max_length=1, choices=GENDER)
  dt_creation = models.DateField(auto_now_add=True)
  dt_modified = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.first_name


class Address(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  country = models.CharField(max_length=50)
  geodiv = models.CharField(max_length=50)
  sub_geodiv = models.CharField(max_length=50)
  geoplace = models.CharField(max_length=50)
  address = models.CharField(max_length=50)
  num = models.IntegerField()
  postal_code = models.IntegerField()
  dt_creation = models.DateField(auto_now_add=True)
  dt_modified = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.address

class serviceProvider(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  isActive = models.IntegerField()
  description = models.TextField()


#Sección para tabajos previos
#class previousJobs (models.Model):

