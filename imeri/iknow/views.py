from django.shortcuts import render
from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseNotFound

from .models import Publication

import csv
from io import StringIO

def home(request):
	return render(request, 'home.html')

def handle_imported_csv(request):
	pass

def import_metadata(request):
	if request.method == 'POST':

		my_file = request.FILES['metadata']
		
		file = my_file.read().decode('utf-8')
		csv_data = csv.reader(StringIO(file), delimiter=',')
		next(csv_data) # ignore 1st line
		try:
			for row in csv_data:
				date_issued = row[6]
				if len(date_issued.split('-')) == 2:
					date_issued += '-01'
				elif len(date_issued.split('-')) == 1:
					date_issued += '-01-01'

				publication = Publication(
					title=row[2],
					authors=", ".join(row[3].split("||")),
					abstract=row[4],
					publisher=row[5],
					date_issued=date_issued, # row[6] yg dimodif
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

		except Exception as e: 
			if 'UNIQUE constraint failed' in str(e):
				#print('masuk unique constraint failed')
				
				return HttpResponse('<h2>Terdapat duplikasi title pada file .csv</h2>')
		
		return render(request, 'import_metadata.html')