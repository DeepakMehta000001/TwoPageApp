from django.db import models

# Create your models here.

class Record(models.Model):
	first_name = models.CharField(max_length=20,default='',blank=False,null=False)
	last_name = models.CharField(max_length=20,default='',blank=False,null=False)
	email = models.EmailField()
	mobile = models.CharField(max_length=20,default='',blank=False,null=False)
	age = models.PositiveIntegerField()
	dob = models.DateField()

def __str__(self):
	return self.email