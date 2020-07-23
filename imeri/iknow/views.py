from django.shortcuts import render
from imeri.iknow.models import Publication

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
		
		#print("my file: ", str(my_file))
		file = my_file.read().decode('utf-8')
		csv_data = csv.reader(StringIO(file), delimiter=',')
		for row in csv_data:
			for i, field in enumerate(row):
				publication = Publication(
					title=row[2],
					authors=", ".join(row[3].split("||")),
					abstract= row[4],
					publisher= row[5],
					date_issued= row[6],
					doi=row[7],
					issn=row[8],
					keywords=", ".join(row[9].split("||")),
					language=row[10],
					type_of=row[11],
					volume=row[12],
					issue_no=row[13],
					pages=row[14],
					uri=row[15],
					video=row[16]
				)

				publication.save()
		
		return render(request, 'import_metadata.html')
	