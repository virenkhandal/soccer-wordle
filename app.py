from flask import *

app = Flask(__name__)

@app.route('/')
def homepage():
    render_template('/static/index.html')


if __name__ == "__main__":
    app.run(debug=True)