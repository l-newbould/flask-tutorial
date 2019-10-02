# flask_app.py
from flask import Flask, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello():
    return "Hello Worlds!"

@app.route("/api")
def j():
	data = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
	json_data = data.to_json(orient='records')
	return json_data

