import csv

with open("CSV\Hospital.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter = '\t')

#print (readCSV) Lopps through data table
for row in readCSV:
    org_code = row[1]
    org_type = row[2]

print(org_code, org_type)
#