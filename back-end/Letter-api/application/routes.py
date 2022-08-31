from application import app
from flask import Flask, request, render_template, url_for
import random 

#letter route 

@app.route("letters/<letter>", methods=['GET'])
def letters(letter):
    user = input("Enter Full Name: ")
    letter = random.choice(user)
    letter=letter.upper()
    print(letter)
characteristics = ("Anticipative", "Brave", "Curious"),("Decisive", "Emotive","Funny" ,"Grounded"),("Home-Bound", "Intelligent", "Jolly", "Knightly"),("Loud", "Melachonly", "Naughty",  "Optimistic", "Patient"),("Quiet", "Restless", "Sad", "Tainted"),("Upright", "Versatile", "Worldly"),("Xenial", "Youthful","Zazzy")
    
if (letter == "A" or letter == "B" or letter == "C"):
    personality = characteristics[0]
    print('Personality:', personality)
elif (letter == "D" or letter == "E" or letter == "F" or letter == "G"):
     personality = characteristics[1]
     print("Personality:", personality)
elif (letter == "H" or letter == "I" or letter == "J" or letter == "K"):
     personality = characteristics[2]
     print("Personality:", personality)
elif (letter == "L" or letter == "M" or letter == "N" or letter == "O" or letter == "P"):
     personality = characteristics[3]
     print("Personality:", personality)
elif (letter == "Q" or letter == "R" or letter == "S" or letter == "T"):
     personality = characteristics[4]
     print("Personality:", personality)
elif (letter == "U" or letter == "V" or letter == "W"):
     personality = characteristics[5]
     print("Personality:", personality)
elif (letter == "X" or letter == "Y" or letter == "Z"): 
     personality = characteristics[6]
     print("Personality:", personality)
else:
    print("Incorrect Name")
    