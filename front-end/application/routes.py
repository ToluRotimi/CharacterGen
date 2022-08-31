from application import app,db
from flask import Flask, render_template, url_for
import requests

# index route
@app.route('/', methods = ['GET'])
def index():
    Letter = requests.get('http://Letter-api:5000/letter')
    Colour = requests.get('http://Colour-api:5000/colour')
    Character = requests.post('http://Character-api:5000/character', json=Letter.json(), json= Colour.json())