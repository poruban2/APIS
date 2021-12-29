from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import mysql.connector as MYSQL

app = Flask(__name__)
CORS(app)

@app.route("/read1", methods=["GET"])
def read1():
    myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
    cursor = myDb.cursor()
#     for line in open(r'./AMOUNTS/SELECT.txt')
        cursor.execute(line)
    cursor.execute('SELECT * FROM Amounts')
    result = cursor.fetchall()
    cursor.close()
    myDb.close()
    vysledok = []
    for i in result:
        vysledok.append(i)
    return jsonify({"Pole":vysledok}),200

@app.route("/read2", methods=["GET"])
def read2():
    myDb = MYSQL.connect(host="147.232.40.14", user ="dn463ri", passwd="Rai0phai", database="dn463ri")
    cursor = myDb.cursor()
    cursor.execute("SELECT * from Amounts")
    result = cursor.fetchall()
    cursor.close()
    myDb.close()
    vysledok = []
    for i in result:
        vysledok.append(f'{i[0]}')
    return jsonify({"Pole":vysledok}),200

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
