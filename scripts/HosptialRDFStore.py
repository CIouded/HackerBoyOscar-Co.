import csv
import rdflib


with open("C:/Users\philn\PycharmProjects\HackerBoyOscar-Co\scripts\Hospital.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter = '\t')

    for row in readCSV:
        hospital_data =[
         row[0], #org ID
         row[1], #org code
         row[2], #org type
         row[3], #subType
         row[4], #org status
         row[5],  #Sector
         row[6], #org statu 2
         row[7], #isPimMang
         row[8], #Org name
         row[9], #Address 1
         row[10], #Address 2
         row[11], #Address 3
         row[12], #City
         row[13], #Country
         row[14], #Postal Code
         row[15], #Lat
         row[16], #Long
         row[17], #AprentODSCode
         row[18], #ParentName
         row[19], #Phone
         row[20], #email
         row[21], #Website

         ]
        #org_ID = row[0]
        #org_code = row[2]

        print(hospital_data)

#print (readCSV) Loops through data table


