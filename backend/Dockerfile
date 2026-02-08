# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos las dependencias e instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código de la app
COPY app.py .

# Exponemos el puerto 5000 (interno del contenedor)
EXPOSE 5000

# Comando para iniciar la app
CMD ["python", "app.py"]
