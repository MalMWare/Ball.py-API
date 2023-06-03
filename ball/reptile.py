from flask import ( Blueprint, render_template )
#import json 

# reptiles = json.load(open(reptiles.json))
# print(reptiles)

bp = Blueprint('reptile', __name__, url_prefix="/reptiles")

@bp.route('/')
def index():
    return render_template('index.html') #reptiles=reptiles)

