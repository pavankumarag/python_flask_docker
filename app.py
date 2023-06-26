from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

@app.route('/new')
def hello_geek_new():
    return '<h1>Hello from Flask /new endpoint</h2>'


if __name__ == "__main__":
    app.run(debug=True)