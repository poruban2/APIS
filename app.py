from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import mysql.connector as MYSQL

app = Flask(__name__)
CORS(app)

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

@app.route("/vytvorit", methods=["POST"])
def create():
    data = request.get_json(force=True)
    data_dict = dict(data)
    myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
    cursor = myDb.cursor()
    cursor.execute("INSERT INTO Amounts (Quantity) VALUES ({})".format(data_dict["vytvorit"]))
    myDb.commit()
    return jsonify("created"),201

@app.route("/upravit/<id>", methods=["PUT"])
def update(id):
    data = request.get_json(force=True)
    data_dict = dict(data)
    myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
    cursor = myDb.cursor()
    cursor.execute("UPDATE Amounts set Price='{}' where AmountID={}".format(data_dict["upravit"], id))
    myDb.commit()
    return jsonify("updated"),201

@app.route("/vymazat/<id>", methods=["DELETE"])
def delete(id):
    data = request.get_json(force=True)
    data_dict = dict(data)
    myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
    cursor = myDb.cursor()
    cursor.execute("DELETE from Amounts where ExtentID={}".format(data_dict["vymazat"], id))
    myDb.commit()
    return jsonify("deleted"),204

if __name__ == "__main__":
    app.run()
