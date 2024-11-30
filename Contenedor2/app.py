from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config
from basededatos import db, init_app, Usuario, Producto
import psycopg2

app = Flask(__name__)
app.config.from_object(Config)
init_app(app)

with app.app_context():
    try:
        db.engine.connect()
        print("Conexión a la base de datos exitosa")
    except Exception as e:
        print("Error al conectar a la base de datos: ", e)

@app.route('/')
def inicio():
    return redirect(url_for('login'))

#pagina principal
@app.route('/index')
def index():
    productos = Producto.query.all()
    return render_template('index.html', productos=productos)

#login y registro
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    print("Entrando en la función login")
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f"Usuario: {username}, Contraseña: {password}")
        usuario = Usuario.query.filter_by(username=username).first()
        if usuario and usuario.password == password:
            print("Login correcto")
            return redirect(url_for('index'))
        else:
            print("Login incorrecto")
            error = "Login incorrecto"
    return render_template('login.html', error=error)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        usuario = Usuario(username=username, password=password, email=email)
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('registro.html')

#CRUD
#crear
@app.route('/productos/crear', methods=['GET', 'POST'])
def crear_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio)
        db.session.add(producto)
        db.session.commit()
        return redirect(url_for('listar_productos'))
    return render_template('productos/crear.html')

#listar
@app.route('/productos')
def listar_productos():
    productos = Producto.query.all()
    return render_template('productos/listar.html', productos=productos)

#editar
@app.route('/productos/<int:id>/editar', methods=['GET', 'POST'])
def editar_producto(id):
    producto = Producto.query.get(id)
    if request.method == 'POST':
        producto.nombre = request.form['nombre']
        producto.descripcion = request.form['descripcion']
        producto.precio = request.form['precio']
        db.session.commit()
        return redirect(url_for('listar_productos'))
    return render_template('productos/editar.html', producto=producto)

#eliminar
@app.route('/productos/<int:id>/eliminar', methods=['POST'])
def eliminar_producto(id):
    producto = Producto.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('listar_productos'))

if __name__ == '__main__':
    app.run(debug=True)