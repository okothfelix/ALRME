from . import frontend_bp
from flask import render_template, redirect, url_for, session, request, jsonify
import web_frontend


@frontend_bp.route('/', methods=['GET'])
def index():
    return render_template('frontend/index.html')


@frontend_bp.route('/get-involved', methods=['GET'])
def get_involved():
    return render_template('frontend/get-involved.html')
