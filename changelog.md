# changelog

## Redis activo

Los tiempos que hemos programado anteriormente son estos:
- **Nginx Caché:** 60 segundos.
- **Redis Caché:** 30 segundos.

**¿Qué ocurre aquí?** Como Nginx guarda la respuesta durante 60 segundos, **nunca llegamos a ver la caché de Redis funcionando** desde fuera, porque la caché de Nginx "tapa" a la de Redis (la de Nginx dura más).

**Para ver la Caché de Redis (Nivel 2) en acción, tendríamos que:**
- Esperar a que expire Nginx (60s).
- Pero para entonces, Redis (30s) también habrá expirado.

El objetivo es que Nginx olvide la respuesta, deje pasar la petición, y Redis diga: "Tranquilo, yo tengo el dato guardado, no hace falta despertar al Backend".

### Reducir la memoria de Nginx
Vamos a hacer que Nginx olvide la caché muy rápido (en 5 segundos en lugar de 60).

- nano nginx/default.conf
```
# Antes: proxy_cache_valid 200 60s;
proxy_cache_valid 200 5s;
```
