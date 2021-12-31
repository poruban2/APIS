from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import mysql.connector as MYSQL

app = Flask(__name__)
CORS(app)

### SELECTS
@app.route("/read_amounts", methods=["GET"])
def read1():
    try:
        myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
        cursor = myDb.cursor()
        file_str = open(r'./AMOUNTS/SELECT.txt').read()
        cursor.execute(file_str, multi=True)
        result = cursor.fetchall()
        cursor.close()
        myDb.close()
        vysledok = []
        for i in result:
            vysledok.append(i)
    except MYSQL.Error as e:
        print(e)
        vysledok = [[1, 2, 3, 4]]
    return jsonify({'Amounts':vysledok}),200

@app.route("/read_extents", methods=["GET"])
def read2():
    try:
        myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
        cursor = myDb.cursor()
        file_str = open(r'./EXTENTS/SELECT.txt').read()
        cursor.execute(file_str, multi=True)
        result = cursor.fetchall()
        cursor.close()
        myDb.close()
        vysledok = []
        for i in result:
            vysledok.append(i)
    except MYSQL.Error as e:
        print(e)
        vysledok = [[1, 2, 3]]
    return jsonify({'Extents':vysledok}),200

@app.route("/read_locations", methods=["GET"])
def read3():
    try:
        myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
        cursor = myDb.cursor()
        file_str = open(r'./LOCATIONS/SELECT.txt').read()
        cursor.execute(file_str, multi=True)
        result = cursor.fetchall()
        cursor.close()
        myDb.close()
        vysledok = []
        for i in result:
            vysledok.append(i)
    except MYSQL.Error as e:
        print(e)
        vysledok = [["Pole1", "Zelena 12", "Lukas Tresa", "+421948925787"]]        
    return jsonify({'Locations':vysledok}),200

### INSERTS
@app.route("/create_amounts", methods=["POST"])
def create1():
    data = request.get_json(force=True)
    data_dict = dict(data)
    myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
    cursor = myDb.cursor()
    file_str = open(r'./AMOUNTS/INSERT.txt').read()
    cursor.execute(file_str.format(data_dict["create_amounts"]), multi=True)
    myDb.commit()
    return jsonify("created"),201

@app.route("/create_extents", methods=["POST"])
def create2():
    data = request.get_json(force=True)
    data_dict = dict(data)
    myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
    cursor = myDb.cursor()
    file_str = open(r'./EXTENTS/INSERT.txt').read()
    cursor.execute(file_str.format(data_dict["create_extents"]), multi=True)
    myDb.commit()
    return jsonify("created"),201

@app.route("/create_locations", methods=["POST"])
def create3():
    data = request.get_json(force=True)
    data_dict = dict(data)
    myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
    cursor = myDb.cursor()
    file_str = open(r'./LOCATIONS/INSERT.txt').read()
    cursor.execute(file_str.format(data_dict["create_locations"]), multi=True)
    myDb.commit()
    return jsonify("created"),201

### UPDATES
@app.route("/update_amounts/<id>", methods=["PUT"])
def update1(id):
    data = request.get_json(force=True)
    data_dict = dict(data)
    myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
    cursor = myDb.cursor()
    file_str = open(r'./AMOUNTS/UPDATE.txt').read()
    cursor.execute(file_str.format(data_dict["update_amounts"], id), multi=True)
    myDb.commit()
    return jsonify("updated"),201

@app.route("/update_extents/<id>", methods=["PUT"])
def update2(id):
    data = request.get_json(force=True)
    data_dict = dict(data)
    myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
    cursor = myDb.cursor()
    file_str = open(r'./EXTENTS/UPDATE.txt').read()
    cursor.execute(file_str.format(data_dict["update_extents"], id), multi=True)
    myDb.commit()
    return jsonify("updated"),201

@app.route("/update_locations/<id>", methods=["PUT"])
def update3(id):
    data = request.get_json(force=True)
    data_dict = dict(data)
    myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
    cursor = myDb.cursor()
    file_str = open(r'./LOCATIONS/UPDATE.txt').read()
    cursor.execute(file_str.format(data_dict["update_locations"], id), multi=True)
    myDb.commit()
    return jsonify("updated"),201

### DELETES
@app.route("/delete_amounts/<id>", methods=["DELETE"])
def delete1(id):
    data = request.get_json(force=True)
    data_dict = dict(data)
    myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
    cursor = myDb.cursor()
    file_str = open(r'./AMOUNTS/DELETE.txt').read()
    cursor.execute(file_str.format(data_dict["delete_amounts"], id), multi=True)
    myDb.commit()
    return jsonify("deleted"),204

@app.route("/delete_extents/<id>", methods=["DELETE"])
def delete2(id):
    data = request.get_json(force=True)
    data_dict = dict(data)
    myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
    cursor = myDb.cursor()
    file_str = open(r'./EXTENTS/DELETE.txt').read()
    cursor.execute(file_str.format(data_dict["delete_extents"], id), multi=True)
    myDb.commit()
    return jsonify("deleted"),204

@app.route("/delete_locations/<id>", methods=["DELETE"])
def delete3(id):
    data = request.get_json(force=True)
    data_dict = dict(data)
    myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
    cursor = myDb.cursor()
    file_str = open(r'./LOCATIONS/DELETE.txt').read()
    cursor.execute(file_str.format(data_dict["delete_locations"], id), multi=True)
    myDb.commit()
    return jsonify("deleted"),204

if __name__ == "__main__":
    app.run()
