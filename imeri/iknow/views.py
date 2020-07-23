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
			print("========================")
		
		return render(request, 'import_metadata.html')
	