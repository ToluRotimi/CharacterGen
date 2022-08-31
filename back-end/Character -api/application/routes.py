from flask import app
from flask import redirect , url_for, render_template

@app.route('/character', methods =["GET","POST"])
def character(colour, personality):
    if (colour == "Red" or colour == "Green" and personality == characteristics[0] or  personality == characteristics[6]):
        message = "Character: Bibbles"
        # insert image
    elif (colour == "Red" or colour == "Green" and personality == characteristics[1] or  personality == characteristics[5]):
        message = "Character: Princess Annelisse "
        # insert image
    elif (colour == "Red" or colour == "Green" and personality == characteristics[2] or  personality == characteristics[4]):
        message = "Character: Princess Genevieve "
        # insert image
    elif (colour == "Red" or colour == "Green" and personality == characteristics[3]):
        message = "Character: Rapunzel "
        # insert image
    elif (colour == "Blue" or colour == "Orange" and personality == characteristics[0] or  personality == characteristics[6]):
        message = "Character: Rapunzel "
        # insert image
    elif (colour == "Blue" or colour == "Orange" and personality == characteristics[1] or  personality == characteristics[5]):
        message = "Character: Princess Genevieve "
        # insert image
    elif (colour == "Blue" or colour == "Orange" and personality == characteristics[2] or  personality == characteristics[4]):
        message = "Character: Princess Annaliese "
        # insert image
    elif (colour == "Blue" or colour == "Orange" and personality == characteristics[3]):
        message = "Character: Bibbles "
        # insert image
    else:
        print ("restart")

    return render_template()
print(function(colour, personality))