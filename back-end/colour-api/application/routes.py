from application import app
from flask import redirect , Response, render_template , request
import random

@app.route('/colour', methods = ["GET"])
def colour():
    colour_list = random.choice(["Red" , "Blue" , "Green" , "Orange"])
    return Response (colour_list,mimetype='text/plain')
