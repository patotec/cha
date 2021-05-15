from django.db import models


class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	message = models.TextField()

	def __str__ (self):
		return self.name

class donation(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	ammount = models.CharField(max_length=200)
	type_of_payment = models.CharField(max_length=200)
	message = models.TextField()

	def __str__ (self):
		return self.name



class post(models.Model):
	CATEGORY_CHOICES = (
    ('C', 'Courses'),
    ('H', 'Help'),
    
)

	name = models.CharField(max_length=200, db_index=True, null=True)
	location = models.CharField(max_length=200,blank=True)
	discription = models.TextField(null=True)
	image = models.ImageField(upload_to='image')
	price = models.FloatField()
	category = models.CharField(choices=CATEGORY_CHOICES, max_length=10 ,null=True)

	def __str__(self):
		return self.name
# Create your models here.
