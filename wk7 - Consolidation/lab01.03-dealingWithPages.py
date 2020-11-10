import requests
import json
from xlwt import *

#The total n. of pages is 14. This code aims to iterate through the pages.

url= "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View"
response = requests.get(url)
data = response.json()
totalPages = data["pagination"]["totalPages"]

listOfReports = []

pageNumber=1
while pageNumber <= totalPages:
    #URL based on the page n.
    pageUrl = url + "&page="+ str(pageNumber)
    
    #Turn the data from the URLs into JSON
    data = requests.get(pageUrl).json()

    #To add into the list
    for item in data["items"]:
        #print(item["ResourceName"])
        listOfReports.append(item["ResourceName"])

    pageNumber +=1



#Output all the reportNames to console

for reportName in listOfReports:
    print(reportName)