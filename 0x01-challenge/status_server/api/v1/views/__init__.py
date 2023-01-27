#!/usr/bin/python3
""" Views module
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from status_server.api.v1.views.index import *
