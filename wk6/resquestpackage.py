import requests

#url = 'https://www.gmit.ie'

# response = requests.get(url)

# print (response.status_code)
# print (response.text) #all the HTML
# print (response.headers) #all the headers info

url = 'http://127.0.0.1:500'
#run the server first

data = {
  'reg': 123,
  'make': 'blah',
  'model':'blah',
  'price': 1234
}

response = requests.post(url,json=data)
print(response.status_code)
print(response.json())