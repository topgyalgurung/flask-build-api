from flask import Flask, make_response, request, jsonify, abort

app = Flask(__name__)
# app=Flask("My First Application")

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

@app.route("/") # default is GET request 
def index():
    return "Hello world "

# first method send custom HTTP code with a tuple 
@app.route("/content")
def no_content():
    return ({"message":"No content found"}, 204)

# second method use make_response method 
@app.route("/exp")
def index_explicit():
     res=make_response({"message": "my first Flask app in action"})
     res.status=200
     return res

# check if variable data exists 
@app.route("/data")
def get_data():
    try:
        if data and len(data) > 0:
            return {"message": f"Data of length {len(data)} found"}
        else:
            return {"message": "Data is empty"}, 500
    except NameError:
        return {"message": "Data not found"}, 404

# Task: create method name_search will not accept parameter, 
# however, will look for the argument q in the incoming request URL. This argument holds the first_name the client is looking for.  
@app.route("/name_search")
def name_search():
    query=request.args.get("q")

    if not query:
        return({"message":"invalid input parameter"},422)
    for person in data:
        if query.lower() in person["first_name"].lower():
            return(person,400)
        
    return({"message:":"Person not found"},404)

# Create a GET /count endpoint 
 # return number of items in the data        
@app.route("/count")
def count():
    try:
        return {"data count": len(data) },200
    except NameError:
        return {"message":"data not defined"},500

# CREATE GET /person/id endpoint
# take argument of type uuid and return person json if found
@app.route("/person/<uuid:id>")
def find_by_uid(id):
   
    for person in data:
        if person["id"]==str(id):
            return person
    return({"message":"person not found"},404)

# CREATE DELETE /person/id endpoint 
@app.route("/person/<uuid:id>",methods=['DELETE'])
def delete_by_uuid(id):
    for person in data:
        if person["id"]==str(id):
            data.remove(person)
            return{"message":f"{id}"},200
    return{"message":"person not found"},404

# Note: problem encountered: method not allowed for requested URL 
# 405 method not allowed error occurs when web server receives a request using HTTP method 
# that does not support or permit the requested resource. 
# causes: misconfigured server or web settings or incorrect code or scripts within app 
# solution: review server configuration, check app code, inspect .htacess and rewrite rules  

# POST Request
# create a new person with details
# client requests with POST method. the method will grab person details from json body ofo post request
@app.route("/person",methods=["POST"])
def add_by_uuid():
    new_person=request.json
    if not new_person:
        return{"message":"invalid input parameter"},422
    # code to validate new_person ommited
    try:
        data.append(new_person)
    except NameError:
        return {"message":"data not defined"},500
    return{"message":f"{new_person['id']}"},200


'''
Flask return HTML page with 404 error if you make an invalid request to server.
But you want to return a JSON response for all invalid requests
the method will return message API not found with 404 whenever client requests a URL that does not lead to any endpoints
defined by server
'''
# did not get expected output need to work on this
@app.errorhandler(404)
def api_not_found(e):
        #return jsonify(error=str(e)),404
       return{"message":"api not found"},404


# if __name__=="__main__":
#     app.run(debug=True)

