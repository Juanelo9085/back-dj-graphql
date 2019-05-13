from django.contrib import admin

#Import models
from . import models
# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.personData)
admin.site.register(models.Address)
admin.site.register(models.serviceProvider)