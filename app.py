from flask import *
import sqlite3
from db import select_random_player
app = Flask(__name__)

@app.route('/')
def homepage():
    data = get_db()
    # render_template('/static/index.html')
    return str(data)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('sqlite.db')
        return select_random_player(db)
    return db

if __name__ == "__main__":
    app.run(debug=True)