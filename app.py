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
    return jsonify({'Amounts':vysledok}),200

@app.route("/read_extents", methods=["GET"])
def read2():
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
    return jsonify({'Extents':vysledok}),200

@app.route("/read_locations", methods=["GET"])
def read3():
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
    return jsonify({'Locations':vysledok}),200

### INSERTS
@app.route("/CreateAmounts", methods=["POST"])
def create1():
    data = request.get_json(force=True)
    myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
    cursor = myDb.cursor()
    file_str = open(r'./AMOUNTS/INSERT.txt').read()
    file_str = file_str.format(data['Quantity'], data['Price'], data['LocationId'], data['ExtentId'])
    cursor.execute(file_str, multi=True)
    myDb.commit()
    cursor.close()
    myDb.close()
    return jsonify("created"),201

@app.route("/CreateExtents", methods=["POST"])
def create2():
    data = request.get_json(force=True)
    myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
    cursor = myDb.cursor()
    file_str = open(r'./EXTENTS/INSERT.txt').read()
    file_str = file_str.format(data['Length'], data['Width'], data['Seedlings'])
    cursor.execute(file_str, multi=True)
    myDb.commit()
    cursor.close()
    myDb.close()    
    return jsonify("created"),201

@app.route("/CreateLocations", methods=["POST"])
def create3():
    data = request.get_json(force=True)
    data_dict = dict(data)
    myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
    cursor = myDb.cursor()
    file_str = open(r'./LOCATIONS/INSERT.txt').read()
    file_str = file_str.format(data['Name'], data['Address'], data['Manager'], data['Contact'])
    cursor.execute(file_str, multi=True)
    myDb.commit()
    cursor.close()
    myDb.close()
    return jsonify("created"),201

### UPDATES
@app.route("/UpdateAmounts/<id>", methods=["PUT"])
def update1(id):
    data = request.get_json(force=True)
    myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
    cursor = myDb.cursor()
    file_str = open(r'./AMOUNTS/UPDATE.txt').read()
    file_str = file_str.format(data['Quantity'], data['Price'], data['LocationId'], data['ExtentId'], id)
    cursor.execute(file_str, multi=True)
    myDb.commit()
    cursor.close()
    myDb.close()
    return jsonify("updated"),201

@app.route("/UpdateExtents/<id>", methods=["PUT"])
def update2(id):
    data = request.get_json(force=True)
    myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
    cursor = myDb.cursor()
    file_str = open(r'./EXTENTS/UPDATE.txt').read()
    file_str = file_str.format(data['Name'], data['Address'], data['Manager'], data['Contact'], id)
    cursor.execute(file_str, multi=True)
    myDb.commit()
    cursor.close()
    myDb.close()
    return jsonify("updated"),201

@app.route("/UpdateLocations/<id>", methods=["PUT"])
def update3(id):
    data = request.get_json(force=True)
    myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
    cursor = myDb.cursor()
    file_str = open(r'./LOCATIONS/UPDATE.txt').read()
    file_str = file_str.format(data['Name'], data['Address'], data['Manager'], data['Contact'], id)
    cursor.execute(file_str, multi=True)
    myDb.commit()
    cursor.close()
    myDb.close()
    return jsonify("updated"),201

### DELETES
@app.route("/DeleteAmounts/<id>", methods=["DELETE"])
def delete1(id):
    myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
    cursor = myDb.cursor()
    file_str = open(r'./AMOUNTS/DELETE.txt').read()
    file_str = file_str.format(id)
    cursor.execute(file_str, multi=True)
    myDb.commit()
    cursor.close()
    myDb.close()
    return jsonify("deleted"),204

@app.route("/DeleteExtents/<id>", methods=["DELETE"])
def delete2(id):
    myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
    cursor = myDb.cursor()
    file_str = open(r'./EXTENTS/DELETE.txt').read()
    file_str = file_str.format(id)
    cursor.execute(file_str, multi=True)
    myDb.commit()
    cursor.close()
    myDb.close()
    return jsonify("deleted"),204

@app.route("/DeleteLocations/<id>", methods=["DELETE"])
def delete3(id):
    myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
    cursor = myDb.cursor()
    file_str = open(r'./LOCATIONS/DELETE.txt').read()
    file_str = file_str.format(id)
    cursor.execute(file_str, multi=True)
    myDb.commit()
    cursor.close()
    myDb.close()
    return jsonify("deleted"),204

if __name__ == "__main__":
    app.run()
