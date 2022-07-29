from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
	return 'Hello TEST2!'


@app.route('/login`')
def login():  # put application's code here
	return 'Login'


if __name__ == '__main__':
	app.run()
