from django.db import models
from django.urls import reverse

# Create your models here.
class tbl_emp(models.Model):
	EmpName = models.CharField(max_length=100)
	Age = models.IntegerField()
	Salary = models.IntegerField()

	def __str__(self):
		return self.EmpName

	def get_absolute_url(self):
		return reverse('home')
