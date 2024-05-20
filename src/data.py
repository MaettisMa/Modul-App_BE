from flask import Flask, json, request
from flask_cors import CORS, cross_origin
from pathlib import Path
import logging
import sys
from utils import *


app = Flask(__name__)
cors = CORS(app,
            origins=["http://localhost:3000", "http://localhost:3000"]
            )
DATA_FOLDER_PATH = Path(
    "/home/matthias/Schreibtisch/Modul_App/modul-app/BE/assets"
)


@app.route("/", methods=["GET"])
def degrees():
    if request.method == "GET":
        data = get_file_data(
            DATA_FOLDER_PATH/"Studiengaenge.json"
        )
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response


@app.route("/20mib", methods=["GET", "PUT", "DELETE", "POST"])
def twenty_mib():
    if request.method == "GET":
        data = get_file_data(
            DATA_FOLDER_PATH/"20mib-module-short.json"
        )
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    elif request.method == "PUT":
        file_path = DATA_FOLDER_PATH/"20mib-module-short.json"
        module = request.data
        index = request.args.get("id")
        update_file(index, module, file_path)
        return "PUT / HTTP/1.1 200"
    elif request.method == "DELETE":
        file_path = DATA_FOLDER_PATH/"20mib-module-short.json"
        index = request.args.get("id")
        delete_module(index, file_path)
        return "DELETE / HTTP/1.1 200"
    elif request.method == "POST":
        file_path = DATA_FOLDER_PATH/"20mib-module-short.json"
        module = request.data
        append_module(module, file_path)
        return "POST / HTTP/1.1 200"



@app.route("/20inb", methods=["GET", "PUT", "DELETE", "POST"])
def twenty_inb():
    if request.method == "GET":
        data = get_file_data(
            DATA_FOLDER_PATH/"20inb-module-short.json"
        )
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    elif request.method == "PUT":
        file_path = DATA_FOLDER_PATH/"20inb-module-short.json"
        module = request.data
        index = request.args.get("id")
        update_file(index, module, file_path)
        return "PUT / HTTP/1.1 200"
    elif request.method == "DELETE":
        file_path = DATA_FOLDER_PATH/"20inb-module-short.json"
        index = request.args.get("id")
        delete_module(index, file_path)
        return "DELETE / HTTP/1.1 200"
    elif request.method == "POST":
        file_path = DATA_FOLDER_PATH/"20inb-module-short.json"
        module = request.data
        append_module(module, file_path)
        return "POST / HTTP/1.1 200"


@app.route("/20mim", methods=["GET", "PUT", "DELETE", "POST"])
def twenty_mim():
    if request.method == "GET":
        data = get_file_data(
            DATA_FOLDER_PATH/"20mim-module-short.json"
        )
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    elif request.method == "PUT":
        file_path = DATA_FOLDER_PATH/"20mim-module-short.json"
        module = request.data
        index = request.args.get("id")
        update_file(index, module, file_path)
        return "PUT / HTTP/1.1 200"
    elif request.method == "DELETE":
        file_path = DATA_FOLDER_PATH/"20mim-module-short.json"
        index = request.args.get("id")
        delete_module(index, file_path)
        return "DELETE / HTTP/1.1 200"
    elif request.method == "POST":
        file_path = DATA_FOLDER_PATH/"20mim-module-short.json"
        module = request.data
        append_module(module, file_path)
        return "POST / HTTP/1.1 200"


@app.route('/20inm', methods=["GET", "PUT", "DELETE", "POST"])
def twenty_inm():
    if request.method == "GET":
        data = get_file_data(
            DATA_FOLDER_PATH/"20inm-module-short.json"
        )
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    elif request.method == "PUT":
        file_path = DATA_FOLDER_PATH/"20inm-module-short.json"
        module = request.data
        index = request.args.get("id")
        update_file(index, module, file_path)
        return "PUT / HTTP/1.1 200"
    elif request.method == "DELETE":
        file_path = DATA_FOLDER_PATH/"20inm-module-short.json"
        index = request.args.get("id")
        delete_module(index, file_path)
        return "DELETE / HTTP/1.1 200"
    elif request.method == "POST":
        file_path = DATA_FOLDER_PATH/"20inm-module-short.json"
        module = request.data
        append_module(module, file_path)
        return "POST / HTTP/1.1 200"

