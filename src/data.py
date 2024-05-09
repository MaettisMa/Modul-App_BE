from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from pathlib import Path
import logging
import sys
import json

app = Flask(__name__)
cors = CORS(app, origins=["http://localhost:3000", "http://localhost:3000"])
DATA_FOLDER_PATH = Path("/home/matthias/Schreibtisch/Modul-App/BE/assets")

# open file
def __get__file__data(file_path):
    with open(file_path) as d:
        file_data = json.load(d)
        return file_data

def __update__file(index_module, updated_module, file_path):
    with open(file_path, 'r+') as f:
        file_data = json.load(f)
        updated_module = json.loads(updated_module.decode('utf-8'))
        i = 0
        while (i < len(file_data)):
            if i == int(index_module):
                file_data[i]['Modul'] = updated_module['Modul']
                file_data[i]['Modulnummer'] = updated_module['Modulnummer']
                file_data[i]['Art'] = updated_module['Art']
                file_data[i]['ECTS'] = updated_module['ECTS']
                file_data[i]['SWS'] = updated_module['SWS']
                file_data[i]['Prüfungsleistung'] = updated_module['Prüfungsleistung']
                print(str(type(file_data)))
                print(str(file_data[i]))
            i = i + 1
        f.seek(0)
        f.truncate() 
        json.dump(file_data, f)

@app.route('/', methods=["GET", "POST"])
def __degrees():
    if request.method == "GET":
        data = __get__file__data(DATA_FOLDER_PATH / "Studiengaenge.json")
        return data, 200
    elif request.method == "POST":
        file_path = DATA_FOLDER_PATH / "Studiengaenge.json"
        module = request.data
        index = request.args.get('id')
        __update__file(index, module, file_path)
        return "POST / HTTP/1.1 200"

@app.route('/20mib', methods=["GET", "POST"])
def __20mib():
    if request.method == "GET":
        data = __get__file__data(DATA_FOLDER_PATH / "20mib-module-short.json")
        return data, 200
    elif request.method == "POST":
        file_path = DATA_FOLDER_PATH / "20mib-module-short.json"
        module = request.data
        index = request.args.get('id')
        __update__file(index, module, file_path)
        return "POST / HTTP/1.1 200"

@app.route('/20inb', methods=["GET", "POST"])
def __20inb():
    if request.method == "GET":
        data = __get__file__data(DATA_FOLDER_PATH / "20inb-module-short.json")
        return data, 200
    elif request.method == "POST":
        file_path = DATA_FOLDER_PATH / "20inb-module-short.json"
        module = request.data
        index = request.args.get('id')
        __update__file(index, module, file_path)
        return "POST / HTTP/1.1 200"

@app.route('/20mim', methods=["GET", "POST"])
def __20mim():
    if request.method == "GET":
        data = __get__file__data(DATA_FOLDER_PATH / "20mim-module-short.json")
        return data, 200
    elif request.method == "POST":
        file_path = DATA_FOLDER_PATH / "20mim-module-short.json"
        module = request.data
        index = request.args.get('id')
        __update__file(index, module, file_path)
        return "POST / HTTP/1.1 200"

@app.route('/20inm', methods=["GET", "POST"])
def __get__20inm():
    if request.method == "GET":
        data = __get__file__data(DATA_FOLDER_PATH / "20inm-module-short.json")
        return data, 200
    elif request.method == "POST":
        file_path = DATA_FOLDER_PATH / "20inm-module-short.json"
        module = request.data
        index = request.args.get('id')
        __update__file(index, module, file_path)
        return "POST / HTTP/1.1 200"
    

