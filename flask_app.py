# flask_app.py
from flask import Flask, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello():
    return "Hello Worlds!"

@app.route("/api")
def j():
	return pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
