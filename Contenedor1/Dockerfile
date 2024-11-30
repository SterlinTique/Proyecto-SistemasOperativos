#Imagen oficial de Python 3.11 como base
FROM python:3.11-slim

# Instalar paquetes necesarios para compilar mysqlclient
RUN apt-get update && apt-get install -y libmariadb-dev-compat libssl-dev pkg-config build-essential

#Establece el directorio de trabajo en el contenedor
WORKDIR /Contenedor1

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias especificadas en requirements.txt
RUN pip install -r requirements.txt

# Instala el comando wait-for-it
RUN apt-get update && apt-get install -y wait-for-it

# Copia el código de tu aplicación al contenedor
COPY . .

# Expose el puerto 5000 para que el contenedor escuche peticiones
EXPOSE 5000

# Establece el comando para ejecutar cuando se inicie el contenedor
CMD ["sh", "-c", "wait-for-it db:3306 --timeout=30 --strict -- echo 'MySQL is up - executing command' && flask run --host=0.0.0.0"]
