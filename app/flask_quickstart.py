from app import app
import os
from flask import (jsonify, json, request, render_template, session)

@app.route('/test', methods=['GET'])
def example():
    #Your Logic Here
    return jsonify('Tudo okay')