from flask import Flask
import logging

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.INFO)

@app.route('/')
def hello_world():
    app.logger.info('inside hello_world method')
    return 'Welcome!'

@app.route('/index')
def index():
    app.logger.info('inside index method')
    return 'Flask Dockerized.'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
