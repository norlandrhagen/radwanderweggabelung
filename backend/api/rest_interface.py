from flask import Flask, jsonify, request, Response

app = Flask(__name__)

'''
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
'''

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)