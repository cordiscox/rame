from rameapp.config import *
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for,redirect,session
from .database import db_session
from . import auth, models
from flask_bootstrap import Bootstrap5
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # create and configure the app
    app = Flask(__name__)
    bootstrap = Bootstrap5(app)
    
    app.config.from_object(DevelopmentConfig)
   
    db.init_app(app)
    migrate.init_app(app, db)

    #@app.route('/')
    #def test():
    #    return render_template('index.html',title='Página de inicio')
    
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    
    app.register_blueprint(auth.bp)

    @app.route('/')
    def home():
        if 'username' in session:
            # Si el usuario está logueado, carga la vista home.html
            return render_template('home.html', username=session['username'])
        else:
            # Si el usuario no está logueado, redirige a la vista de inicio de sesión
            return redirect(url_for('auth.login'))
   
    return app



