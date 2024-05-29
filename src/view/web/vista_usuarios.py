from flask import Flask, Blueprint, render_template, request, redirect, url_for

blueprint = Blueprint( "vista_usuarios", __name__, "templates" )

import sys
sys.path.append("src")
sys.path.append(".")
from model.user import Usuario
import controller.app_controller as app_controller

controlador_usuarios = app_controller.ControladorUsuarios()
controlador_hipotecas = app_controller.ControladorHipotecas()

app = Flask(__name__)


@blueprint.route("/")
def Home():
   return render_template("index.html")

@blueprint.route( "/nuevo-usuario")
def VistaNuevoUsuario():
   return render_template("nuevo-usuario.html")

@blueprint.route("/crear-usuario", methods=['POST'])
def crear_usuario_view(): #create
    nombre = request.form.get("nombre")
    edad = request.form.get("edad")
    if edad:
        edad = int(edad)  
    try:
        usuario = controlador_usuarios.crear_usuario(nombre, edad)
        return render_template("usuario.html", user=usuario, mensaje="Usuario insertado exitosamente!")
    except ValueError as e:
        return render_template("excepcion.html", mensaje_error=str(e))
    except Exception as e:
        return render_template("excepcion.html", mensaje_error=f"Error: {str(e)}")

@blueprint.route("/lista-usuarios")
def lista_usuarios(): #select
    try:
        usuarios = controlador_usuarios.obtener_usuarios()
        return render_template("lista-usuarios.html", usuarios=usuarios)
    except Exception as e:
        return render_template("excepcion.html", mensaje_error=f"Error al obtener usuarios: {str(e)}")

   
@blueprint.route("/eliminar-usuario/<int:usuario_id>", methods=['POST'])
def eliminar_usuario(usuario_id):
    try:
        controlador_usuarios.eliminar_usuario(usuario_id)
        return redirect(url_for('vista_usuarios.lista_usuarios'))
    except Exception as e:
        return render_template("excepcion.html", mensaje_error=str(e))
    

@blueprint.route("/modificar-usuario/<int:usuario_id>", methods=['POST'])
def modificar_usuario_view(usuario_id):
    nombre = request.form.get("nombre")
    edad = request.form.get("edad")
    if edad:
        edad = int(edad)  # Asegurarse de que la edad es un número
    try:
        controlador_usuarios.modificar_usuario(usuario_id, nombre, edad)
        return redirect(url_for('vista_usuarios.lista_usuarios'))
    except Exception as e:
        return render_template("excepcion.html", mensaje_error=str(e))
    
@blueprint.route("/modificar-usuario/<int:usuario_id>", methods=['GET'])
def vista_modificar_usuario(usuario_id):
    try:
        usuario = controlador_usuarios.obtener_usuario_por_id(usuario_id)
        if usuario is None:
            raise Exception("El usuario no existe")
        return render_template("modificar-usuario.html", usuario=usuario)
    except Exception as e:
        return render_template("excepcion.html", mensaje_error=str(e))
