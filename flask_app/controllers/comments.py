from dataclasses import dataclass
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import athlete, coach
from flask_app.controllers import athletes, coaches