
# Not a script for running
# Example of how to import data to a model
# These line are what I actually wrote to the python interactive shell: python3 manage.py shell

from qmh.models import Patient
from csv import reader

# with open('data/superspreadsheet_simplified-20190722.csv', 'r', newline='') as f:
# 	rows = reader(f, delimiter=',', quotechar='"')
# 	for row in list(rows)[1:]:# skips header; list() converts csv_object to list_object, only use list() if the csv is small
# 		if not row[7].isdigit():
# 			row[7]=0
# 		Patient.objects.update_or_create(patientNumber=str(row[0].replace(',', '')), firstName=str(row[1]), lastName=str(row[2]), gender=str(row[3]), admitDateFull=str(row[4]), admitYear=str(row[5]), admitMonth=str(row[6]), admitAge=str(row[7]), leaveDateFull=str(row[8]))

with open('data/admission_book_v_1_1817-1885 - data.csv', 'r', newline='') as f:
	rows = reader(f, delimiter=',', quotechar='"')
	for row in list(rows)[1:]:# skips header; list() converts csv_object to list_object, only use list() if the csv is small
		if not row[7].isdigit():
			row[7]=0
		Patient.objects.update_or_create(dateOfLastAdmission=str(row[0].replace(',', '')), numberInOrderOfAdmission=str(row[1]), dateOfAdmission=str(row[2]), fullName=str(row[3]), age=str(row[4]), race=str(row[5]), sex=str(row[6]), nativity=str(row[7]), civilConditionMarriage=str(row[8]))
