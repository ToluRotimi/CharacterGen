from application import app
from flask import redirect , url_for, render_template,Response,jsonify,request

@app.route('/character', methods =["POST"])
def character():
    data_sent = request.get_json()
    if data_sent["colour"] == "Red" or data_sent["colour"] == "Green" and data_sent["personality"] == "Anticipative""Brave""Curious" or  data_sent["personality"] == "Xenial""Youthful""Zazzy":
        message = "Character: Bibbles"
        # insert image
    elif data_sent["colour"] == "Red" or data_sent["colour"] == "Green" and data_sent["personality"] == "Decisive""Emotive""Funny""Grounded" or data_sent["personality"]  == "Upright""Versatile""Worldly":
        message = "Character: Princess Annelisse "
        # insert image
    elif data_sent["colour"]== "Red" or data_sent["colour"] == "Green" and data_sent["personality"] == "Home-Bound""Intelligent""Jolly""Knightly" or data_sent["personality"]  == "Quiet""Restless""Sad""Tainted":
        message = "Character: Princess Genevieve "
        # insert image
    elif data_sent["colour"] == "Red" or data_sent["colour"] == "Green" and data_sent["personality"] == "Loud""Melachonly""Naughty""Optimistic""Patient":
        message = "Character: Rapunzel "
        # insert image
    elif data_sent["colour"] == "Blue" or data_sent["colour"] == "Orange" and data_sent["personality"] == "Anticipative""Brave""Curious" or  data_sent["personality"] == "Xenial""Youthful""Zazzy":
        message = "Character: Rapunzel "
        # insert image
    elif data_sent["colour"] == "Blue" or data_sent["colour"] == "Orange" and data_sent["personality"] == "Decisive""Emotive""Funny""Grounded" or data_sent["personality"]  == "Upright""Versatile""Worldly" :
        message = "Character: Princess Genevieve "
        # insert image
    elif data_sent["colour"] == "Blue" or data_sent["colour"] == "Orange" and data_sent["personality"] == "Home-Bound""Intelligent""Jolly""Knightly" or data_sent["personality"]  == "Quiet""Restless""Sad""Tainted":
        message = "Character: Princess Annaliese "
        # insert image
    elif data_sent["colour"] == "Blue" or data_sent["colour"] == "Orange" and data_sent["personality"] == "Loud""Melachonly""Naughty""Optimistic""Patient":
        message = "Character: Bibbles "
        # insert image
    else:
        message = " we got to the else statement"
    return Response(message,mimetype='text/plain')

