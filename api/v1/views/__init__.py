#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint
from api.v1.views.index import *
from api.v1.views.cities import *
from api.v1.views.states import *

app_views = Blueprint("base", __name__, url_prefix="/api/v1")
