import json
from flask import request, abort, Response
from flask.ext import restful
from flask.ext.restful import reqparse
from flask_rest_service import app, api
from models.YOLO_small_tf import YOLO_TF

ALLOWED_EXTENSIONS = ["png","jpg","jpeg"]
model = YOLO_TF()

def allowed_file(fn):
    return '.' in fn and fn.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

class CarCounter(restful.Resource):

	def get(self):
		print "testing model ..."
		return model.test_predict("test/car.jpg")

	def post(self):
		print "recieved image to classify ..."
		if "image" in request.files and allowed_file(request.files["image"].filename):
			return model.predict(request.files["image"])
		else:
			return Response(status=500)

api.add_resource(CarCounter, '/count-cars')
