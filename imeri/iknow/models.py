from django.db import models
# from django_mysql.models import ListCharField

class Publication(models.Model):
	
	
	"""
	authors = ListCharField(
		base_field=CharField(max_length=100),
		size=6,
		max_length=(6 * 11)  # 6 * 10 character nominals, plus commas
	)
	"""
	title = models.CharField(max_length=500, unique=True)
	authors = models.CharField(max_length=500)
	abstract = models.CharField(max_length=50000)
	publisher = models.CharField(max_length=500)
	volume = models.IntegerField()
	issue_no = models.CharField(max_length=500)
	pages = models.CharField(max_length=500)
	issue_date = models.DateField()
	doi = models.CharField(max_length=500)
	uri = models.CharField(max_length=500)
	issn = models.CharField(max_length=500)
	keywords = models.CharField(max_length=500)
	type_of = models.CharField(max_length=500)

	def __str__(self):
		return self.title

	#class Meta:
	#	delimiter = ','