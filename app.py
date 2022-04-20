from flask import Flask, render_template
from controllers.controller import books_blueprint

app = Flask(__name__)

app.register_blueprint(books_blueprint)