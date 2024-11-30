import mysql.connector

def conectar():
    return mysql.connector.connect(
        host='db:3306',
        user='root',
        password='password',
        database='contenedor1'
    )