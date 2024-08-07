from flask import Flask


app = Flask(__name__)


@app.route('/')

def home():
    return "<center><h1>hello world!<center>"


if __name__ == '__main__':
    app.run(debug=True)
