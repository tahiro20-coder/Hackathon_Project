from flask_restful import Api, Resource, reqparse
from flask import Flask, send_from_directory,current_app,jsonify,request
import requests as req
import numpy as np
import math as mt
import json

API_KEY  = "blBXxEYF7eYX0h3O17rtVZOc0REp0RW6"
class Chat(Resource):
    def get(self):
        return {
        'message': "recycle Get"
        }

    def post(self):
        print(self)
        
        # matrix_2 = np.array(request.json["matrix2"])

        # context = request.args.getlist('context')[0]
        context = ""
        question =  request.json["question"]

        url = "https://api.ai21.com/studio/v1/j2-ultra/chat"
        
        payload = {
            "numResults": 1,
            "temperature": 0.7,
            "messages": [
                {
                    "text": question,
                    "role": "user"
                }
            ],
            "system": "You are an AI assistant for recycling garbage. Your responses should be informative and concise."

        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f'Bearer {API_KEY}'
        }

        response = req.post(url, json=payload, headers=headers)

        data = json.loads(response.text)
        
        return {"output":data["outputs"][0]["text"]}