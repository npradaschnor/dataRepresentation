import json

data = {
  'name': 'Joe',
  'age': 21,
  'student': True

}

file = open("simple.json","w")
# json.dumps(data,file, indent=4) 
# dumps json into the file indented

jsonString = json.dumps(data) #uses to get a string and passes it into a server
print(jsonTring)
