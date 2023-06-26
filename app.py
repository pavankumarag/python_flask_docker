import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return f"<h2>Hello from Flask & Docker from pod: {os.environ.get('HOSTNAME', 'DEFAULT_ENV')} </h2>"
os
@app.route('/new')
def hello_geek_new():
    return f"<h1>Hello from Flask /new endpoint from pod: {os.environ.get('HOSTNAME', 'DEFAULT_ENV')} </h2>"


if __name__ == "__main__":
    app.run(debug=True)