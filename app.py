from flask import Flask, send_from_directory,current_app,jsonify,request,render_template
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.main import Chat,Recycle
import os
import sys

app = Flask(__name__, static_url_path='', static_folder='fronted/build')
CORS(app, origins=['https://smart-recycle.onrender.com'], methods=['GET', 'POST'], support_credentials=True)#comment this on deployment
api = Api(app)



@app.route("/", defaults={'path':''})
def serve(path):
    print(app.static_folder)
    
    return send_from_directory(app.static_folder,'index.html')

api.add_resource(Chat, '/chat')
api.add_resource(Recycle, '/recycle')