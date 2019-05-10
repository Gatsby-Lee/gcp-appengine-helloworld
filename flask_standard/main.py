from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Flask - GoogleAppEngine(GAE) Standard'


if __name__ == '__main__':
    app.run(debug=True)
