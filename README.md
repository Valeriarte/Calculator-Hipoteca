# Calculadora de hipoteca inversa.

El proyecto consiste en desarrollar una aplicación en Python
que permita calcular la cuota mensual que un banco le pagaría 
a una persona que ha adquirido una hipoteca inversa.

## Integrantes del grupo:
- Valeria Solarte Jiménez
- Jhair Santamaria

## Estructura del proyecto:
- src: Contiene la lógica de negocio (model), las interfaces gráficas y el controlador (controller).
- tests: Contiene las pruebas unitarias del aplicativo.
- sql: Contiene los scripts sql para crear las tablas necesarias para el correcto funcionamiento del controlador.

## Prerrequisitos
- Asegurese de tener instalado Python en su unidad. Si no lo tiene instalado, puede visitar el siguiente link y descargar el ejecutable: [Python](https://www.python.org/).

- Crear una base de datos PostgreSQL y configurar los respectivos datos de acceso.

- Instalar psycopg2 con el comando: pip install psycopg2

- Instalar flask con el comando: pip install flask

# Database
Requisitos:
Asegúrese de tener una base de datos PostgreSQL y sus respectivos datos de acceso. Modifique el archivo SecretConfig-Sample.py a secret_config.py e ingrese en este archivo los datos de conexión a su base de datos.

Establezca el puerto 5432 que es por defecto.

-PGHOST='xxx'

-PGDATABASE='xxxx'

-PGUSER='xxxxx'

-PGPASSWORD='xxx'

-PGPORT = 'xxx'

Configuración de la base de datos
Esta aplicación requiere que esté creada dos tablas llamadas:
- Usuarios 
- Hipotecas 

Utilice los scripts con el comando sql\tabla_usuarios.sql y sql\tabla_hipotecas.sql para crearla antes de ejecutar la aplicación.


## ¿Cómo se usa?
Para hacer uso del aplicativo asegurese de tener instalado las dependencias necesarias. Una vez tenga las dependencias necesarias prosiga con las instrucciones:

1. Clone el repositorio en su unidad y abra la consola de comandos. Ejecute el siguiente comando: `set PYTHONPATH=[ruta de la carpeta raiz clonada]`. Ignore los corchetes, por ejemplo, en mi caso el comando quedaría de la siguiente manera: `set PYTHONPATH=C:\Users\dsana\Workspace\Calculator-Hipoteca`. Cabe recalcar que debe ser ejecutado en una terminal cmd (consola de comandos) y no en una powershell.

2. Ubiquese en la raiz de la carpeta clonada. Use el comando `cd [ruta de la carpeta]`.

3. Si desea correr las pruebas unitarias del modelo del aplicativo:
    - Ubiquese en la carpeta 'tests' de la ruta clonada.
    - Ejecute el siguiente comando: `python tests.py`.

4. Si desea ejecutar las pruebas del controlador:
    - Ubiquese en la carpeta 'tests' de la ruta clonada.
    - Ejecute el siguiente comando: `python controller_tests.py`

5. Si desea ejecutar la interfaz por consola:
    - Ubiquese en la siguiente ruta 'src/view/console'.
    - Ejecute el siguiente comando: `python controller_console.py`

6. Si desea ejecutar la interfaz gráfica de usuario (gui):
    - Ubiquese en la siguiente ruta: 'src/view/interface'.
    - Ejecute el siguiente comando: `python interface.py`.

7. Si desea ejecutar la pagina web:
    - Para ejecutar la pagina web desde la carpeta del programa, use el comando:

      Calculator-Hipoteca>python app.py

    - Luego de haber ejecutado presiona CTRL+C al local host http://127.0.0.1:5000

    Nota: Antes de calcular la hipoteca, primero crea el usuario y para poder ver la lista de hipotecas
    tienes que ingresar en /lista-hipotecas/ primero el id de la hipoteca, cuando haya
    cargado la pagina lo borras e ingresas y el id del usuario



