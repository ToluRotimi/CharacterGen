from application import app
from flask import redirect , url_for, render_template

@app.route('/character', methods =["GET","POST"])
def character(colour, personality):
    if colour == "Red" or colour == "Green" and characteristics == characteristics[0] or  characteristics == characteristics[6]:
        message = "Character: Bibbles"
        # insert image
    elif colour == "Red" or colour == "Green" and characteristics == characteristics[1] or  characteristics == characteristics[5]:
        message = "Character: Princess Annelisse "
        # insert image
    elif colour == "Red" or colour == "Green" and characteristics == characteristics[2] or  characteristics == characteristics[4]:
        message = "Character: Princess Genevieve "
        # insert image
    elif colour == "Red" or colour == "Green" and characteristics == characteristics[3]:
        message = "Character: Rapunzel "
        # insert image
    elif colour == "Blue" or colour == "Orange" and characteristics == characteristics[0] or  characteristics == characteristics[6]:
        message = "Character: Rapunzel "
        # insert image
    elif colour == "Blue" or colour == "Orange" and characteristics == characteristics[1] or  characteristics == characteristics[5]:
        message = "Character: Princess Genevieve "
        # insert image
    elif colour == "Blue" or colour == "Orange" and characteristics == characteristics[2] or  characteristics == characteristics[4]:
        message = "Character: Princess Annaliese "
        # insert image
    elif colour == "Blue" or colour == "Orange" and characteristics == characteristics[3]:
        message = "Character: Bibbles "
        # insert image
    else:
        message = " we got to the else statement"
    return Response(message,mimetype='text/plain')
