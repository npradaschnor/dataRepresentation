#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response

app = Flask(__name__,
            static_url_path='', 
            static_folder='../')

#Saved in memory:array for storing the cars
cars = [
    {
        "reg":"181 G 1234",
        "make":"Ford",
        "model":"Modeo",
        "price":18000
    },
    {
        "reg":"11 MO 1234",
        "make":"Nissan",
        "model":"Almera",
        "price":8000
    },
    {
        "reg":"test",
        "make":"Nissan",
        "model":"Almera",
        "price":8000
    }
]

#url map for /cars for method GET
#returns the list converted in JSON
@app.route('/cars', methods=['GET'])
def get_cars():
    return jsonify( {'cars':cars})
# curl -i http://localhost:5000/cars

#To find the ID by passing the info to the function as a String called 'reg'
@app.route('/cars/<string:reg>', methods =['GET'])
def get_car(reg):
    foundCars = list(filter(lambda t : t['reg'] == reg , cars))#filter searches through the list cars and returns only the ones that matches the reg variable. lambda goes through each element of the list
    if len(foundCars) == 0:
        return jsonify( {'car' : '' }),204 #if nothing is returned send back an empty car, with status 204
    return jsonify( {'car' : foundCars[0] }) #otherwise send back a JSON object - the 1st of the found cars
#curl -i http://localhost:5000/cars/test

@app.route('/cars', methods=['POST'])
def create_car():
    if not request.json:
        abort(400) #check that the request has JSON data (if not returns a 400 error)
    if not 'reg' in request.json:
        abort(400)
    car={
        "reg":  request.json['reg'],
        "make": request.json['make'],
        "model":request.json['model'],
        "price":request.json['price']
    } #read the request object and create a new car
    cars.append(car) #append it to the list car
    return jsonify( {'car':car }),201 #returns what was just added

# sample test
# curl -i -H "Content-Type:application/json" -X POST -d "{\"reg\":\"12 D 1234\",\"make\":\"Fiat\",\"model\":\"Punto\",\"price\":3000}' http://localhost:5000/cars

#This is a put and it takes in the reg from the url
@app.route('/cars/<string:reg>', methods =['PUT'])
def update_car(reg):
    foundCars=list(filter(lambda t : t['reg'] ==reg, cars)) #searches through the list of cars using lambda function
    if len(foundCars) == 0:
        abort(404) #if car is not found
    if not request.json:
        abort(400) #check if the JSON in the request is properly formatted
    if 'make' in request.json and type(request.json['make']) != str:
        abort(400) #if make is not a type of string returns 400 error
    if 'model' in request.json and type(request.json['model']) is not str:
        abort(400) #if model is not a type of string returns 400 error
    if 'price' in request.json and type(request.json['price']) is not int:
        abort(400) #if price is not a type of number
    foundCars[0]['make']  = request.json.get('make', foundCars[0]['make'])
    foundCars[0]['model'] =request.json.get('model', foundCars[0]['model'])
    foundCars[0]['price'] =request.json.get('price', foundCars[0]['price'])
    return jsonify( {'car':foundCars[0]}) #returns the updated car

#curl -i -H "Content-Type:application/json" -X PUT -d '{"make":"Fiesta"}' http://localhost:5000/cars/181%20G%201234
#curl -i -H "Content-Type:application/json" -X PUT -d "{\"make\":\"Fiesta\"}" http://localhost:5000/cars/181%20G%201234

#Similar to previous functions. using the lambda function to find the car by the reg variable. If found it is deleted and it returns a JSON that says the result is True 
@app.route('/cars/<string:reg>', methods =['DELETE'])
def delete_car(reg):
    foundCars = list(filter (lambda t : t['reg'] == reg, cars))
    if len(foundCars) == 0:
        abort(404)
    cars.remove(foundCars[0])
    return  jsonify( {'result':True })

#Handles error 404 and 400
@app.errorhandler(404)
def not_found404(error):
    return make_response(jsonify( {'error':'Not found' }), 404)

@app.errorhandler(400)
def not_found400(error):
    return make_response(jsonify( {'error':'Bad Request'}), 400)


if __name__ == '__main__' :
    app.run(debug= True)#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response

app = Flask(__name__,
            static_url_path='', 
            static_folder='../')

cars = [
    {
        "reg":"181 G 1234",
        "make":"Ford",
        "model":"Modeo",
        "price":18000
    },
    {
        "reg":"11 MO 1234",
        "make":"Nissan",
        "model":"Almera",
        "price":8000
    },
    {
        "reg":"test",
        "make":"Nissan",
        "model":"Almera",
        "price":8000
    }
]

@app.route('/cars', methods=['GET'])
def get_cars():
    return jsonify( {'cars':cars})
# curl -i http://localhost:5000/cars

@app.route('/cars/<string:reg>', methods =['GET'])
def get_car(reg):
    foundCars = list(filter(lambda t : t['reg'] == reg , cars))
    if len(foundCars) == 0:
        return jsonify( { 'car' : '' }),204
    return jsonify( { 'car' : foundCars[0] })
#curl -i http://localhost:5000/cars/test

@app.route('/cars', methods=['POST'])
def create_car():
    if not request.json:
        abort(400)
    if not 'reg' in request.json:
        abort(400)
    car={
        "reg":  request.json['reg'],
        "make": request.json['make'],
        "model":request.json['model'],
        "price":request.json['price']
    }
    cars.append(car)
    return jsonify( {'car':car }),201
# sample test
# curl -i -H "Content-Type:application/json" -X POST -d '{"reg":"12 D 1234","make":"Fiat","model":"Punto","price":3000}' http://localhost:5000/cars
# curl -i -H "Content-Type:application/json" -X POST -d "{\"reg\":\"12 D 1234\",\"make\":\"Fiat\",\"model\":\"Punto\",\"price\":3000}' http://localhost:5000/cars

@app.route('/cars/<string:reg>', methods =['PUT'])
def update_car(reg):
    foundCars=list(filter(lambda t : t['reg'] ==reg, cars))
    if len(foundCars) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'make' in request.json and type(request.json['make']) != str:
        abort(400)
    if 'model' in request.json and type(request.json['model']) is not str:
        abort(400)
    if 'price' in request.json and type(request.json['price']) is not int:
        abort(400)
    foundCars[0]['make']  = request.json.get('make', foundCars[0]['make'])
    foundCars[0]['model'] =request.json.get('model', foundCars[0]['model'])
    foundCars[0]['price'] =request.json.get('price', foundCars[0]['price'])
    return jsonify( {'car':foundCars[0]})
#curl -i -H "Content-Type:application/json" -X PUT -d '{"make":"Fiesta"}' http://localhost:5000/cars/181%20G%201234
#curl -i -H "Content-Type:application/json" -X PUT -d "{\"make\":\"Fiesta\"}" http://localhost:5000/cars/181%20G%201234


@app.route('/cars/<string:reg>', methods =['DELETE'])
def delete_car(reg):
    foundCars = list(filter (lambda t : t['reg'] == reg, cars))
    if len(foundCars) == 0:
        abort(404)
    cars.remove(foundCars[0])
    return  jsonify( { 'result':True })

@app.errorhandler(404)
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)


if __name__ == '__main__' :
    app.run(debug= True)