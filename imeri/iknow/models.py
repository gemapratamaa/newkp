from django.db import models
from django_mysql.models import ListCharField

# Create your models here.
class Person(models.Model):
    title = models.CharField(max_length=300)
	
	"""
	authors = ListCharField(
        base_field=CharField(max_length=100),
        size=6,
        max_length=(6 * 11)  # 6 * 10 character nominals, plus commas
    )
	"""
	authors = models.CharField(max_length=500)
	abstract = models.CharField(max_length=50000)
	publisher = models.CharField(max_length=500)
	volume = models.IntegerField

    last_name = models.CharField(max_length=30)