from django.db import models

#from location_field.models.plain import PlainLocationField

# Create your models here.

from geoposition.fields import GeopositionField

class Record(models.Model):
	first_name = models.CharField(max_length=20,default='',blank=False,null=False)
	last_name = models.CharField(max_length=20,default='',blank=False,null=False)
	email = models.EmailField()
	mobile = models.CharField(max_length=20,default='',blank=False,null=False)
	age = models.PositiveIntegerField()
	dob = models.DateField()
	#place = models.CharField(max_length=50,default='',blank=False,null=False)
	location = GeopositionField(null=False)



def __str__(self):
	return self.email