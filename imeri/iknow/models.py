from django.db import models

class Publication(models.Model):
	title = models.CharField(max_length=500, unique=True)
	authors = models.CharField(max_length=500)
	abstract = models.CharField(max_length=50000)
	publisher = models.CharField(max_length=500)
	date_issued = models.DateField()
	doi = models.CharField(max_length=500)
	issn = models.CharField(max_length=500)
	keywords = models.CharField(max_length=500)
	language = models.CharField(max_length=500, default='en')
	type_of = models.CharField(max_length=500)
	volume = models.IntegerField()	
	issue_no = models.CharField(max_length=500)
	pages = models.CharField(max_length=500)
	uri = models.CharField(max_length=500)
	video = models.CharField(max_length=500, default='')

	def __str__(self):
		return self.title