# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** (nombre que se le ha dado al modelo) 
> **Epsilon-Support Vector Regression OceanHeatMLFlow:** SVR para predecir flujo de calor utilizando datos de grosor sedimentario.
- **Plataforma de despliegue:** (plataforma donde se va a desplegar el modelo)
> El modelo será implementado y desplegado en un entorno local a través de una API utilizando FastAPI. FastAPI es un marco de desarrollo web de Python que permite construir rápidamente aplicaciones web de alto rendimiento y escalables.
- **Requisitos técnicos:** (lista de requisitos técnicos necesarios para el despliegue, como versión de Python, bibliotecas de terceros, hardware, etc.)
> - **Versión de Python:** python 3.11.3
> - **Librerias:** fastapi(0.98.0), pydantic(1.10.9), joblib(1.2.0), typing(4.6.3)
> - **Software:** Linux base OS (Manjaro Linux X86_64), kernel 6.2.16-MANJARO
> - **Hardware:** CPU: 11th Gen Intel i7-1195G7 (8) @ 5.000GHz, GPU: Intel TigerLake-LP GT2 [Iris Xe Graphics], RAM: 31804MiB
- **Requisitos de seguridad:** (lista de requisitos de seguridad necesarios para el despliegue, como autenticación, encriptación de datos, etc.)
> Validación de entrada de datos: Realiza una validación con `pydantic` de los datos de entrada enviados a la API. Esto incluye la verificación de tipos de datos. Al asegurarte de que los datos de entrada cumplan con los criterios esperados para prevenir ataques de inyección y garantizar la integridad de los datos.
- **Diagrama de arquitectura:** (imagen que muestra la arquitectura del sistema que se utilizará para desplegar el modelo)


## Código de despliegue

- **Archivo principal:** (nombre del archivo principal que contiene el código de despliegue)
- **Rutas de acceso a los archivos:** (lista de rutas de acceso a los archivos necesarios para el despliegue)
- **Variables de entorno:** (lista de variables de entorno necesarias para el despliegue)

## Documentación del despliegue

- **Instrucciones de instalación:** (instrucciones detalladas para instalar el modelo en la plataforma de despliegue)
- **Instrucciones de configuración:** (instrucciones detalladas para configurar el modelo en la plataforma de despliegue)
- **Instrucciones de uso:** (instrucciones detalladas para utilizar el modelo en la plataforma de despliegue)
- **Instrucciones de mantenimiento:** (instrucciones detalladas para mantener el modelo en la plataforma de despliegue)
