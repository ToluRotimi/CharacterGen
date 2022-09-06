from application import app
from flask import Flask, request,render_template, url_for
import requests

# index route
@app.route('/', methods = ['GET'])
def index():
    personality = requests.get('http://personality-api:5001/personality').text
    colour = requests.get('http://colour-api:5002/colour').text
    character = requests.post('http://character-api:5003/character', json = {"personality": personality, "colour":colour})
    return render_template('characters.html',personality=personality,colour=colour,character=character.text)