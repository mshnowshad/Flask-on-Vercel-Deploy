from flask import Flask


app = Flask(__name__)


@app.route('/')

def home():
    return "<h1>hello world!"


if __name__ == '__main__':
    app.run(debug=True)