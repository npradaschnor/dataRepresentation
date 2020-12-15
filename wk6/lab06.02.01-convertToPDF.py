import requests
import json

f = open(r"C:\Users\User\Desktop\GMIT\DATA REPRESENTATION\wk1 - XML, HTML, DOM\carviewer.html","r")
html = f.read()

apiKey = '29dd6faa14d3489764c43c32cda3c406f46e892ff01fb2617210a12844c643bb'
url = 'https://api.html2pdf.app/v1/generate'

data = {'html':html, 'apiKey':apiKey}
response = requests.post(url, json=data)

newFile = open("lab06.02.01htmlaspdf.pdf", "wb")
newFile.write(response.content)
print(response.status_code)