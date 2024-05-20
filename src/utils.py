from flask import json

def get_file_data(file_path):
    with open(file_path) as file_:
        file_data = json.load(file_)
        return file_data


def update_file(index_module, updated_module, file_path):
    with open(file_path, "r+") as file_:
        file_data = json.load(file_)
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
        file_.seek(0)
        file_.truncate()
        json.dump(file_data, file_)


def delete_module(index_module, file_path):
    with open(file_path, "r+") as file_:
        file_data = json.load(file_)
        file_data.pop(int(index_module))
        file_.seek(0)
        file_.truncate()
        json.dump(file_data, file_)