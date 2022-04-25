# airflow_local
- Este proyecto tiene como objetivo levantar una instancia
 de Airflow de forma local de la forma más rápida y sencilla
 para usuarios de Windows

## Instalar Docker for Desktop

Ingresar al [Siguiente Link](https://docs.docker.com/desktop/windows/install/)
 y seleccionar el cartel azul **Docker Desktop for Windows**

## Ejecutar los comandos dentro del directorio del proyecto

Clonar el repositorio y abrir la carpeta *airflow_local*
 en su editor de texto preferido (Yo utilizo Visual Studio Code)

Correr el siguiente comando para inicializar la base de datos
```bash
docker-compose up airflow-init
```

Al finalizar el comando, se deberían identificar las siguientes líneas
```
airflow-init_1       | Upgrades done
airflow-init_1       | Admin user airflow created
airflow-init_1       | 2.2.5
start_airflow-init_1 exited with code 0
```

Para levantar el servicio, simplemente ejecutar
```
docker-compose up
```