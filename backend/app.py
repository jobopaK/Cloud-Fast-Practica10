from flask import Flask
import redis
import time
import os

app = Flask(__name__)

# Conexión a Redis.
# IMPORTANTE: 'host="redis"' funcionará porque en docker-compose llamaremos al servicio "redis".
cache = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def index():
    try:
        # Intentamos obtener el dato de la caché de Redis (Nivel 2)
        dato = cache.get('dato_pesado')

        if dato:
            # Si existe, lo devolvemos rápido
            return f"Respuesta desde REDIS (Caché L2 Backend): {dato}\n"

        else:
            # Si NO existe, simulamos el proceso pesado
            time.sleep(3) # Simula carga de trabajo de 3 segundos
            resultado = "Datos procesados tras espera de 3s"

            # Guardamos en Redis por 30 segundos para la próxima vez
            cache.set('dato_pesado', resultado, ex=30)

            return f"Respuesta desde PROCESO (Generado ahora): {resultado}\n"

    except redis.exceptions.ConnectionError:
        return "Error: No se pudo conectar con el contenedor de Redis.\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
