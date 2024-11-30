# Proyecto de login y CRUD con Flask y MariaDB - SistemasOperativos

Este proyecto es realizado con el fin de lograr y poner a prueba conceptos viste en Sistemas Operativos, el proyecto consta de un sistema básico de cómo crear una aplicación web con Flask y MariaDB que incluya un sistema de login y un CRUD (Crear, Leer, Actualizar, Eliminar) para gestionar usuarios, el fin de este proyecto es poder ser aislado en un contenedor mediante una imagen Docker, para ser ejcutado en cualquier ordenador.

## Requisitos

* Flask
* PostgreSQL
* Python 3.x

## Funcionalidades

* Sistema de Login con Registro
* Sistema CRUD 

## Responsables

* Jader Sterlin Tique Medina.
* Sebastian Quintero Montoya.

## Instalación

### Instalación y ejecución sin Docker

1. Clona el repositorio en tu máquina local.
2. Crea un entorno virtual con `python -m virtualenv env` (opcional).
2. 1. Enciende el entorno virtual con `.\env\Scripts\activate`.
2. 2. Cuando finalices apaga tu entorno virtual con `deactivate`.
3. Instala las dependencias necesarias con `pip install -r requirements.txt`.
4. Crea una base de datos en MariaDB y configura la conexión en el archivo `config.py`.
5. Ejecuta la aplicación con `python app.py`.

### Instalación y ejecución con Docker

1. Descargar la imagen Docker.
2. Abre la aplicación Docker Desktop en tu máquina local.
3. Crear un nuevo contenedor utilizando la imagen Docker.
4. Configura las opciones del contenedor según sea necesario. 
5. Iniciar el contenedor.
6. Accede a la aplicación utilizando la URL y el puerto configurados. 


## Uso

1. Accede a la aplicación en `http://localhost:5000` o `http://127.0.0.1:5000`.
2. Registra un nuevo usuario en la página de registro.
3. Inicia sesión con el usuario registrado.
4. Accede al CRUD para gestionar productos.



## Nota

* Si al ejecutar `pip list` en el entorno virtual le sale un error, utilice este este comando `pip install --upgrade setuptools`. Aunque no es un error que tome demasiada importancia, aquí esta la solución por si se llega a presentar.