#Imagen oficial de Python 3.11 como base
FROM python:3.11-slim

#Establece el directorio de trabajo en el contenedor
WORKDIR /Contenedor2

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias especificadas en requirements.txt
RUN pip install -r requirements.txt

# Copia el código de tu aplicación al contenedor
COPY . .

# Expose el puerto 5000 para que el contenedor escuche peticiones
EXPOSE 5000

# Establece el comando para ejecutar cuando se inicie el contenedor
CMD ["flask", "run", "--host=0.0.0.0"]