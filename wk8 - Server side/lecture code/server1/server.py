from flask import Flask, url_for, request, redirect, abort

app = Flask(__name__, static_url_path='', static_folder='staticpages')

#redirect index page to /login URL
@app.route('/')
def index():
   return  redirect(url_for('login'))

#when /login is acessed the 401 (unauthorized) error appears
@app.route('/login')
def login():
    abort(401)
    return "served by Login"

@app.route('/user')
def getUser():
    return "served by getUser"

@app.route('/user/<int:id>')
def findByIdUser(id):
    return "served by findByIdUser with id = "+str(id)

@app.route('/user', methods=['POST'])
def createUser():
    return "served by createUser"

@app.route("/demo_url_for")
def demoUrlFor():
    returnString = "url For index is "+ url_for('index')
    returnString += "<br/>"
    returnString += "url for findByIdUser "+ url_for('findByIdUser', id=12)
    return returnString

#curl -X POST http://127.0.0.1:500/
#curl -X GET http://127.0.0.1:500/
#curl -X DELETE http://127.0.0.1:500/

@app.route("/demo_request", methods=['POST', 'GET', 'DELETE'])
def demoRequest():
    return request.method

#run Flask
if __name__ == "__main__":
    print("in if")
    app.run(debug=True)