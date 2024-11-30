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

### Instalación y ejecución con Docker Desktop

#### Requisitos previos
##### Instalación de WSL (Windows Subsystem for Linux)
1. Abre la busqueda de Windows y busca `Activar o desactivar la características de Windows`.
2. Activa el `Subsistema de Windows para Linux` WSL y `Plataforma de máquina virtual`.
3. Reinicia tu computadora.
##### Instalación de un entorno de Linux para WSL
1. Abre la Tienda de Microsoft en Windows.
2. Busca "Linux" en la barra de búsqueda.
3. Selecciona la distribución de Linux que deseas instalar (por ejemplo, Ubuntu).
4. Haz clic en "Instalar".
5. Sigue las instrucciones para completar la instalación.
##### Instalación de Docker Desktop
1. Abre el sitio web de Docker Desktop en un navegador web.
2. Haz clic en "Descargar para Windows (Stable)".
3. Sigue las instrucciones para completar la instalación.
4. Reinicia tu computadora.
##### Configuración de Docker Desktop
1. Abre la aplicación Docker Desktop en Windows.
2. Haz clic en el icono de engranaje en la esquina superior derecha.
3. Selecciona `Preferencias` en el menú desplegable.
4. Haz clic en la pestaña "WSL".
5. Activa la opción `Habilitar la integración de WSL 2`.
6. Selecciona la distribución de Linux que instalaste.
7. Haz clic en "Guardar y reiniciar".

####  Intalación y ejcución
1. Clona el repositorio en tu máquina local.
2. Abre la Terminal de WSL y posiciónate en la carpeta de cada contendor.
3. Crea la imagen con `docker-compose build` y inicialó con `docker-compose up`.
4. Abre la aplicación Docker Desktop en tu máquina local y confirma que el contenedor esta iniciado.
5. Configura las opciones del contenedor según sea necesario.
6. Accede a la aplicación utilizando la URL y el puerto configurados.

## Uso

1. Accede a la aplicación en `http://localhost:5000` o `http://127.0.0.1:5000`.
2. Registra un nuevo usuario en la página de registro.
3. Inicia sesión con el usuario registrado.
4. Accede al CRUD para gestionar productos.



## Nota

* Si al ejecutar `pip list` en el entorno virtual le sale un error, utilice este este comando `pip install --upgrade setuptools`. Aunque no es un error que tome demasiada importancia, aquí esta la solución por si se llega a presentar.