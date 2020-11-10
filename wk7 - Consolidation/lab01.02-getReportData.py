import requests
import json

#Library to generate spreadsheet files compatible with Microsoft Excel
from xlwt import *


url= "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=>2019-11-10"
response = requests.get(url)
data = response.json()

listOfReports = []

for item in data["items"]:
    listOfReports.append(item["ResourceName"])

#Create a spreadsheet
w = Workbook()
ws = w.add_sheet('rows')
rowNumber = 0;
ws.write(rowNumber,0,"StartTime")
ws.write(rowNumber,1,"EndTime")
ws.write(rowNumber,2,"ImbalanceVolume")
ws.write(rowNumber,3,"ImbalancePrice")
ws.write(rowNumber,4,"ImbalanceCost")
rowNumber += 1

for ReportName in listOfReports:
    url ="https://reports.sem-o.com/api/v1/documents/"+ReportName
    response= requests.get(url)
    aReport= response.json()
    for row in aReport["rows"]:
        #Get the info from the array "rows" and save it in a spreadsheet named balance.xls
        ws.write(rowNumber,0,row["StartTime"])
        ws.write(rowNumber,1,row["EndTime"])
        ws.write(rowNumber,2,row["ImbalanceVolume"])
        ws.write(rowNumber,3,row["ImbalancePrice"])
        ws.write(rowNumber,4,row["ImbalanceCost"])
        rowNumber += 1
w.save('balance.xls')