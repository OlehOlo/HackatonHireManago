from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
	return 'TEST!'


if __name__ == '__main__':
	app.run()
