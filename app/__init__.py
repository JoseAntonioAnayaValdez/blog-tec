import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv 

#Cargar las variables de entorno
load_dotenv()

#crear instancia
app =  Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Master#117@localHost/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#importar models
from app.models.post import Post
from app.models.category import Category
# Importar blueprints
from app.routes.post import post_bp

with app.app_context():
    # Crear las tablas en la base de datos
    db.create_all()

# Registrar blueprints
app.register_blueprint(post_bp, url_prefix='/posts')

#ruta principal
@app.route('/')
def index():
    return render_template('index.html')
