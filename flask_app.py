# flask_app.py
from flask import Flask, jsonify, request
import pandas as pd 

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello():
    return "Hello Worlds!"

@app.route("/api", methods=["POST", "GET"])
def j():
	if request.methods == "POST": 
		post_data = request.form.to_dict(flat=False)
		print(post_data)
		post_data_df = pd.DataFrame(post_data)
		print(post_data_df)
		post_data_json = post_data_df.to_json(orient='records')
		print(post_data_json)
		return post_data_json

	else if request.methods == "GET":
		post_data = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}).to_json(orient='records')
		return post_data

