# chat conversation
import json
import pymysql
import requests
import http.client
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from itertools import cycle

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["POST"])
@cross_origin()
def function(self):
    load_dotenv()
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_DDBB = os.getenv("DB_DDBB")
    #try:
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_DDBB)
    cursor = connection.cursor()

    print("conexión exitosa")
    id = str(request.json['id'])

    sql = "select id, nombre, apellido, telefono, email, contrasena, fecha_nacimiento, genero, tipo_usuario, status from usuarios where tipo_usuario='profesional' and id='"+id+"';"
    cursor.execute(sql)
    resp = cursor.fetchall()
    print(str(resp))

    arrayUsers=[]
    retorno = {
        "users":{}
    }
    for registro in resp:
        item={
            "id":registro[0],
            "nombre":registro[1],
            "apellido":registro[2],
            "telefono":registro[3],
            "email":registro[4],
            #"contrasena":registro[5],
            "fecha_nacimiento":registro[6],
            "genero":registro[7],
            "tipo_usuario":registro[8],
            "status":registro[9]
        }
        arrayUsers.append(item)
    retorno['users'] = arrayUsers
    return retorno

    #except Exception as e:
    #    print('Error: '+ str(e))
    #    retorno = {           
    #        "detalle":"algo falló", 
    #        "validacion":False
    #    }
    #    return retorno

if __name__ == "__main__":
    app.run(debug=True, port=8002, ssl_context='adhoc')