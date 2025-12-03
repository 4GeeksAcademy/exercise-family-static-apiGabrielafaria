import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object
jackson_family = FamilyStructure("Jackson")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET','POST'])
def handle_members():
    #If method is POST
    if request.method == 'POST':
        response_body = jackson_family.add_member(request.get_json())
        return response_body, 200
    else:
        members = jackson_family.get_all_members()
        #If the response is a list we return it
        if isinstance(members,list):
            response_body = members
            return jsonify(response_body), 200
        #If not we return the error
        else:
            return "Status: Members could not be fetched", 400


@app.route('/members/<int:id>', methods=['GET','DELETE'])
def handle_get_member(id):
    #If method is DELETE
    if request.method == 'DELETE':
        response_body = jackson_family.delete_member(id)
    else:
        response_body = jackson_family.get_member(id)
    #If the response is a dict we return it
    if isinstance(response_body, dict):
        return jsonify(response_body), 200
    #If not we return the error
    else:
        return response_body, 400



# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)