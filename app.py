from flask import Flask, send_from_directory,current_app,jsonify,request,render_template
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.main import Recycle
import sys

app = Flask(__name__, static_url_path='', static_folder='fronted/build')
CORS(app, origins=['https://easy-algebra.onrender.com'], methods=['GET', 'POST'], allow_headers=['Content-Type']) #comment this on deployment

api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    print(app.static_folder)
    return send_from_directory(app.static_folder,'index.html')


api.add_resource(Recycle, '/Recycle')