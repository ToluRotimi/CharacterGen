from application import app
from flask import Flask, request,render_template, url_for
import requests

# index route
@app.route('/', methods = ['GET'])
def index():
    personality = requests.get('http://personality-api:5001/personality')
    colour = requests.get('http:/colour-api:5002/colour')
    character = requests.post('http://character-api:5003/character', json = {"Letters": Letter.text, "Colours":Colour.text})
    # Character.data.decode