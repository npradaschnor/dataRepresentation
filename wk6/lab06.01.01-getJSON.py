import requests
import json
from xlwt import *

url = "http://127.0.0.1:500/cars"

response = requests.get(url)
data = response.json()

#output to console
print(data)

#output cars individually
for car in data["cars"]:
  print(car)

#save this to a file
filename = 'cars.json'

if filename:
  #writing json data
  with open(filename,'w') as f:
    json.dump(data,f,indent=4)

#writing to excel file
w = Workbook() #make a new workbook
ws = w.add_sheet('cars') #add a new spreadsheet
row = 0
ws.write(row,0,"reg") #row 0, col 1
ws.write(row,1,"make")
ws.write(row,2,"model")
ws.write(row,3,"price")

row +=1

for car in data["cars"]: #for each of the car in the array cars
  ws.write(row,0,car["reg"]) #store reg in row 0,col 1
  ws.write(row,1,car["make"])
  ws.write(row,2,car["model"])
  ws.write(row,3,car["price"])
  row +=1

w.save('cars.xls') #save as cars.xls
