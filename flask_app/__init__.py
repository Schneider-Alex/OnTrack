from flask import Flask, session
app = Flask(__name__)
from flask_app import secret_key

app.secret_key = secret_key.secret_key