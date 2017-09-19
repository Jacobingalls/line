# -*- coding: utf-8 -*-
import random
import re
import datetime
from flask import Flask, render_template, jsonify, request, send_from_directory
app = Flask(__name__)

reservation_index = 0
reservations=[]

@app.route("/api/reservations", methods=["GET", "POST"])
def get_reservations():
	global reservation_index

	if request.method == "GET":
		return jsonify({"reservations": reservations})
	else:
		reservation = {
			"id": reservation_index,
			"created": datetime.datetime.now(),
			"name": request.json["name"],
			"state": "Waiting"
		}

		reservations.append(reservation)
		reservation_index += 1
		return jsonify({"reservation": reservation})

@app.route("/api/reservations/next", methods=["POST"])
def goto_next_reservation():

	for i in [r for r in reservations if r["state"] == "Helping"]:
		i["state"] = "Helped"

	waiting = [r for r in reservations if r["state"] == "Waiting"]
	if len(waiting) > 0:
		waiting[0]["state"] = "Helping"


	return jsonify({"reservations": reservations})


@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)



if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")
