 
from flask import render_template

import sys
sys.path.append("src")
sys.path.append(".")
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

from view.web import vista_usuarios 

app = Flask(__name__)     

app.register_blueprint( vista_usuarios.blueprint )


if __name__=='__main__':
   app.run( debug=True )