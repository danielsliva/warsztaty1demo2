from flask import Flask
from names import namesgenerator

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/generate')
def generate_random_name():
    return namesgenerator.get_random_name()


if __name__ == '__main__':
    app.run()
