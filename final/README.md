# Iniciemos

1. Clonar el repositorio https://github.com/Jenicilla/challenge.git en la maquina local `git clone https://github.com/Jenicilla/challenge.git`
2. Abrir una terminal e ingresar a la ruta challenge/final/
3. Ejecutar el archivo install.sh `./install.sh` el cual va a aprovisionar todos los paquetes necesarios para la ejecución del  entorno virtual que contiene la solución y a su vez, le da iniciar la API.
4. Abrir otra terminal, dirigirse a la ruta challenge/final/ donde se encuentra el archivo consumerExterno.py y ejecutarlo `python3 consumerExterno.py`, para consumir los datos del EndPoint público https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios y guardarlos en la base de datos local. 
5. Para el escenario de listar todos los datos, consumir la URL http://127.0.0.1:5000/tasks en un navegador.
6. Para el escenario de listar solo un dato a la vez, consumir la URL http://127.0.0.1:5000/tasks/one?id=1 en un navegador, modificando el registro que se encuentra después del signo =.