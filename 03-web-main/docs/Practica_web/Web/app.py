from turtle import end_fill
from flask import Flask, jsonify, request
from flask.helpers import send_file
from datetime import datetime, timedelta
from time import sleep
from random import randint
import io
import os
import sys
import requests
import json
from urllib3.exceptions import NewConnectionError
from datetime import datetime
from datetime import timedelta

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
	return send_file('web/index.html')


@app.route('/datos.html')
def datosUsuario():
	return send_file('web/view/datos.html')

@app.route('/registro.html')
def registro():
	return send_file('web/view/registro.html')

@app.route('/view/script.js')
@app.route('/script.js')
def scripts_script():
	return send_file('web/view/script.js')

@app.route('/view/login.css')
def style_login():
	return send_file('web/view/login.css')

@app.route('/datos.css')
def style_datos():
	return send_file('web/view/datos.css')

@app.route('/register.css')
def style_register():
	return send_file('web/view/register.css')


@app.route('/login', methods=['POST'])
def login():
	if request.is_json:
		username = request.json.get('username', None)
		password = request.json.get('password', None)
	
		if not username:
			return jsonify({"msg": "Missing username parameter"}), 400
		if not password:
			return jsonify({"msg": "Missing password parameter"}), 400
	else:
		username = request.form['username']
		password = request.form['password']
		
	try:
		
		end = datetime.now()
		start = end - timedelta(days=28)
		endStr = str(end)
		startStr = str(start)
		listaend = endStr.split()
		listastart = startStr.split()
		
		r = requests.post("http://localhost:8080/api/rest/login?username={}&password={}".format(username,password),
				headers={"x-hasura-admin-secret":"myadminsecretkey"})
		data = r.json()
		user = data["users"]
		datos = user[0]

		r = requests.get("http://localhost:8080/api/rest/user_access_log/"+datos["uuid"]+"/daterange", 
  			headers={"x-hasura-admin-secret":"myadminsecretkey"}, 
  			json={"startdate": listastart[0]+"T00:00:00+00:000", "enddate": listaend[0]+"T00:00:00+00:000"})
		data = r.json()
		facilities = data["access_log"]

		list_facilities = []
		for facility in facilities:
			data_set = {"name": facility["facility"]["name"]}
			json_list = json.dumps(data_set)
			list_facilities.append(json_list)
		print(list_facilities)

		return jsonify({"datos" : datos, "access_log" : list_facilities}), 200
	except requests.exceptions.ConnectionError as http_err:
		return jsonify({"error": "Connection Error"}), 500
	except:
		return jsonify({"error": "Usuario no encontrado"}), 401	

@app.route('/register', methods=['POST'])
def register():
	try:
		r = requests.post(
		"http://localhost:8080/api/rest/user",
		headers={"x-hasura-admin-secret":"myadminsecretkey"},
		data={"username": request.form['user'], "password": request.form['password'], "name": request.form['name'], "surname": request.form['surname'], 
				"phone":  request.form['phone'], "email":  request.form['email'], "is_vaccinated":  request.form['vacunado']})
		data = r.json()
		datos = data["insert_users_one"]
		return jsonify({"all_good": "Usuario creado"}), 200
	except requests.exceptions.ConnectionError as http_err:
		print("error de http")	
		return jsonify({"error": "Connection Error"}), 500
	except:
		return jsonify({"error": "No se puede crear usuario"}), 401
	




		
