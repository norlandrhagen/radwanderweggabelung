from flask import Flask, jsonify, request, Response
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


"""
GET:    Trail
        Trail_Metadata
        Section
        User
        User_Metadata
        Run

POST:   Trail
        Trail_Metadata
        Section
        User
        Run      
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
