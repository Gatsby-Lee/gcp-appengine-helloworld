import flask

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    flask_version = flask.__version__
    return 'Flask %s - GoogleAppEngine(GAE) Standard - v1.3' % flask_version


if __name__ == '__main__':
    app.run(debug=True)
