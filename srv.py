from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime
import uuid


app = Flask(__name__)
CORS(app)


t_ids = {}

@app.route('/')
def home():
	print("hello")
	return jsonify({"Working": True})

@app.route('/okk')
def ok():
	print("hi")
	return jsonify({"ok": 'ok'})


@app.route('/create_room', methods=['POST', 'GET'])
def create_room():
	data = request.json
	t_id = str(data['t_id'])
	if t_id in t_ids:
		return jsonify({"msg": 't_id already exists', 'ok': 1, "t_id": t_id})
	else:
		t_ids[t_id] = {}
	return jsonify({"status": 'ok', "t_id": t_id})


@app.route('/join_room', methods=['POST', 'GET'])
def join_room():
	data = request.json
	t_id = data['t_id']
	c_id = data['c_id']
	name = data['name']

	if t_id not in t_ids:
		return jsonify({"ok": 0, 'msg':'Incorrect T_ID', "t_id": t_id})

	if c_id in t_ids[t_id]:
		return jsonify({"ok": 1, 'msg':'Alredy In That Room', "t_id": t_id})

	t_ids[t_id][c_id] = {
		"pp": 0,
		"code": 'USER DID NOT WRITE ANYTHING',
		"push": "",
		"name": name
	}
	return jsonify({"status": 'Successfully Joined', 'ok': 1, "t_id": t_id})



@app.route('/clear', methods=['POST', 'GET'])
def clear():
	t_ids.clear()
	return jsonify({"clear": "done!" })

@app.route('/info', methods=['POST', 'GET'])
def info():
	return jsonify(t_ids)

@app.route('/ping')
def ping():
	return jsonify({"pong": datetime.now().isoformat()})

# import sys
# try:
# 	port =  sys.argv[1]
# except :
# 	port = 5000

# 
# 
# port = int(port)
# if __name__ == '__main__':
# 	app.run(host='0.0.0.0', port=port, debug=True, threaded=True)