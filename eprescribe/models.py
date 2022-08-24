from django.db import models


class PrescribeMed(models.Model):
	physcian = models.CharField(max_length=50)
	entry_date = models.DateField(auto_now_add=True)
	prescription = models.TextField()
	patient_name = models.CharField(max_length=50)

	def __str__(self):
		return self.physcian