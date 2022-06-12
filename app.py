from flask import *
import sqlite3
from db import select_random_player
app = Flask(__name__)

@app.route('/')
def homepage():
    data = get_db()
    # player = data[0]
    return render_template('index.html', player=data)
    # return str(data)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('sqlite.db')
        return select_random_player(db)
    return db

if __name__ == "__main__":
    app.run(debug=True)