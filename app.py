from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import mysql.connector as MYSQL

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def main():
    myDb = MYQSQL.connect(host="147.232.40.14", user ="rp805bv", passwd="eiGh5thi", database="rp805bv")
    cursor = myDb.cursor()
    cursor.exectue("SELECT Nazov, Uroda from Pole")
    result = cursor.fetchall()
    cursor.close()
    myDb.close()
    vysledok = []
    for i in result:
        vysledok.append('{'+'{}'.format(i[0])+'}')
    return jsonify({"Pole":vysledok}),200

@app.route("/vytvorit", methods=["POST"])
def create():
    data = request.get_json(force=True)
    data_dict = dict(data)
    myDb = MYQSQL.connect(host="147.232.40.14", user ="rp805bv", passwd="eiGh5thi", database="rp805bv")
    cursor = myDb.cursor()
    cursor.exectue("INSERT INTO Pole (Nazov) VALUES ({})".format(data_dict["vytvorit"]))
    myDb.commit()
    return jsonify("created"),201

@app.route("/upravit/<id>", methods=["PUT"])
def update(id):
    data = request.get_json(force=True)
    data_dict = dict(data)
    myDb = MYQSQL.connect(host="147.232.40.14", user ="rp805bv", passwd="eiGh5thi", database="rp805bv")
    cursor = myDb.cursor()
    cursor.exectue("UPDATE Pole set Nazov='{}' where ID={}".format(data_dict["upravit"], id))
    myDb.commit()
    return jsonify("updated"),201

@app.route("/vymazat/<id>", methods=["DELETE"])
def delete(id):
    data = request.get_json(force=True)
    data_dict = dict(data)
    myDb = MYQSQL.connect(host="147.232.40.14", user ="rp805bv", passwd="eiGh5thi", database="rp805bv")
    cursor = myDb.cursor()
    cursor.exectue("DELETE from Pole where ID={}".format(data_dict["vymazat"], id))
    myDb.commit()
    return jsonify("deleted"),204

if __name__ == "__main__":
    app.run()
