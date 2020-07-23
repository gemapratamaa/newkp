from django.shortcuts import render

import csv
from io import StringIO

def home(request):
	return render(request, 'home.html')

	
def handle_imported_csv(request):
	pass


def import_metadata(request):
	if request.method == 'POST':# and request.FILES['metadata']:
		print("masuk post")

		my_file = request.FILES['metadata']
		
		print("my file: ", str(my_file))
		file = my_file.read().decode('utf-8')
		csv_data = csv.reader(StringIO(file), delimiter=',')
		for row in csv_data:
			for i, field in enumerate(row):
				print(i, field)
				title = row[2]
				authors = ", ".join(row[3].split("||"))
				abstract = row[4]
				publisher = row[5]
				type_of = row[11]
				
				volume = models.IntegerField()
				issue_no = models.CharField(max_length=500)
				pages = models.CharField(max_length=500)
				issue_date = models.DateField()
				doi = models.CharField(max_length=500)
				uri = models.CharField(max_length=500)
				issn = models.CharField(max_length=500)
				keywords = models.CharField(max_length=500)
				type_of = models.CharField(max_length=500)
				video = models.CharField(max_length=500)
			print("========================")
		
		return render(request, 'import_metadata.html')
	