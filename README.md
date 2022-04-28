# airflow_local
- Este proyecto tiene como objetivo levantar una instancia
 de Airflow de forma local de la forma más rápida y sencilla
 para usuarios de Windows


## Instalar Docker for Desktop

- Ingresar al [Siguiente Link](https://docs.docker.com/desktop/windows/install/)
y seleccionar el cartel azul **Docker Desktop for Windows**

- Hay que comprobar que esté activado en **Características de Windows** la opción de
**Plataforma de máquina virtual** y **Subsistema de Windows para Linux**
  - No es necesario tener plataforma del hipervisor de Windows activado

![enablewsl](./resources/enablewsl.png)

- En caso de que nos salga el siguiente error:
```
The current user is not in the 'docker-users' group. Add yourself to the 'docker-users' group and then log out and back in to Windows.
```

- Abrir "Command Prompt" como administrador y ejecutar el siguiente comando (Al abrir Command Prompt
podemos ver el valor de \<DOMAIN> por defecto **antes** de ingresar nuestras credenciales de administrador):
```
net localgroup docker-users <DOMAIN>\<username> /add
```
- "Sign out" para cerrar nuestra sesión. Ingresar de nuevo en la pantalla de inicio (también se puede reiniciar).


- En caso de que Docker Desktop tire el error de WSL 2 installation is incomplete, descargar del [Siguiente link](https://aka.ms/wsl2kernel)
la actualización del kernel para el subsistema de Linux.

![wsl2kernelupdate](./resources/wsl2kernelupdate.png)

- En caso que salga el error de Assisted Hardware virtualization se debe reiniciar la computadora,
entrar a la BIOS y activar Hardware assisted virtualization. Si tienen la PC en español
esta opción se llama de forma diferente, generalmente se identifica con la palabra "virtualización"
y podemos ver que dice Desactivado. En una laptop HP yo tuve que apretar F10.

![hardwareassisvirtual](./resources/hardwareassisvirtual.png)


## Ejecutar los comandos dentro del directorio del proyecto

Clonar el repositorio y abrir la carpeta *airflow_local*
en su editor de texto preferido (Yo utilizo Visual Studio Code)

![clonetherepo](./resources/clonetherepo.png)

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
Esperar a que se levanten los servicios e ingresar a la web en http://localhost:8080 ó http://127.0.0.1:8080

Para detener Airflow, ejecutar en la terminal:
```
docker-compose down
```
Cada vez que abrimos Docker Desktop, se aloca ~2GB de memoria
para usar el backend de Windows Subsystem for Linux. Para detenerlo:
```
wsl --shutdown
```