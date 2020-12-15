import requests
import json

# remove the minus sign
# this API key no longer works, probably because someone saved it to GitHub
# I have made a new one and posted to  learnonline
apiKey = '9f48324719785bbb8009b96370106e88677cd047'
url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne'
https://github.com/npradaschnor/aPrivateOne
filename = "repo.json"

response = requests.get(url, auth=('token', apiKey))

repoJSON = response.json()
#print (response.json())

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)

#

url = "https://github.com/npradaschnor/Pima-Indians-Diabetes-Dataset"

#if the website requests a username and password
#response = requests.get(url, auth=(user, pswd))

response = requests.get(url)

#checking the status code for the url
print (response.status_code)

#checking encoding used to decode
rencod = response.encoding
print(rencod)

#saving the website content to a file
with open('pima.txt', 'wb') as file:
    file.write(response.content)
