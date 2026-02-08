# Cloud-Fast (Practica 10)

## 1. Contexto del Proyecto
La empresa **"Cloud-Fast"** necesita modernizar su arquitectura de servicios. Actualmente, sus aplicaciones corren de forma aislada y sufren cuellos de botella cuando el volumen de peticiones aumenta.

Como administrador de sistemas de **SAD**, se te ha encomendado desplegar un entorno - **completamente contenedorizado** que solucione tres pilares fundamentales:
- **Seguridad Perimetral**: Ningún servicio (API o Base de Datos) debe estar expuesto directamente, salvo el Proxy.
- **Rendimiento**: Implementación de una estrategia de caché de dos niveles (Capa de Red y Capa de Aplicación).
- **Portabilidad y Disponibilidad**: Todo el entorno debe ser reproducible mediante orquestación básica de contenedores.

## 2. Objetivos de la Práctica (RA 5 y RA 6)
- Desplegar un escenario de microservicios utilizando **Docker Compose.**
- Configurar **Nginx** como Proxy Inverso y servidor de caché de objetos.
- Implementar **Redis** como almacén de datos persistentes en memoria para el backend.
- Asegurar la red interna de contenedores para cumplir con los principios de **Seguridad Activa.**

## 3. Requisitos de la Infraestructura
El alumno deberá configurar un entorno compuesto por tres contenedores interconectados:

### A. Contenedor de Proxy (Nginx)
- Debe ser el único servicio con puertos mapeados al Host (Puerto 80).
- Debe actuar como **Proxy Inverso** hacia el contenedor de la API.
- **Reto:** Configurar una zona de caché (`proxy_cache`) que almacene las respuestas de la API durante 60 segundos para evitar tráfico innecesario hacia el backend.

### B. Contenedor de Aplicación (API Backend)
- Debe ejecutar un servicio (Python/Flask preferiblemente) que no sea accesible desde el exterior.
- **Lógica de negocio:** La API debe simular un proceso pesado (2-3 segundos de espera) antes de devolver un dato.
- **Integración:** La API debe consultar primero a Redis antes de realizar el "proceso pesado".

### C. Contenedor de Datos (Redis)
- Debe funcionar como base de datos en memoria.
- Solo debe aceptar conexiones provenientes de la red interna de Docker creada para la práctica.

## 4. Tareas a realizar
- **Definición de Orquestación:** Crear el archivo `docker-compose.yml` que defina los tres servicios y sus dependencias.
- **Configuración del Proxy:** Redactar el archivo `.conf` para Nginx que gestione el balanceo/redirección y la lógica de caché de nivel 1.
- **Desarrollo del Backend:** Implementar el código necesario para que la aplicación gestione la lógica de "Caché de nivel 2" con Redis.
- **Seguridad de Red:** Definir una red privada en Docker donde convivan los contenedores.
