import requests
import json


#url = "https://reports.sem-o.com/api/v1/documents/static-reports"

#Balancing and Impalance Market Cost Report from Date 10-11-2019
url= "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=>2019-11-10"

#Get the info from the URL
response = requests.get(url)
data = response.json()

#Create a list
listOfReports = []


#Get all the ResourceName in items and add them to listOfReports list
for item in data["items"]:
    listOfReports.append(item["ResourceName"])

#Create an URL for each ReportName, get each URL and returns a JSON object
for ReportName in listOfReports:
    url ="https://reports.sem-o.com/api/v1/documents/"+ReportName
    print(url)
    response= requests.get(url)
    aReport= response.json()

#Save this to a file named allreports.json
filename = 'allreports.json'
# Writing JSON data
f =  open(filename, 'w')
json.dump(data, f, indent=4)