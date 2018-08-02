from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class Irq(Resource):
    def get(self, irq_number):
        f = open("/proc/interrupts", "r")
        contents = f.read()
        return contents, 200

api.add_resource(Irq, "/irq/<string:irq_number>")

app.run(debug=True, host='0.0.0.0', port=80)
