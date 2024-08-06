from . import frontend_bp
from flask import render_template, redirect, url_for, session, request, jsonify
import web_frontend


@frontend_bp.route('/', methods=['GET'])
def index():
    return render_template('frontend/index.html')


@frontend_bp.route('/contacts', methods=['POST'])
def contacts():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    result_set = web_frontend.user_contact_section(name, email, message)
    if result_set:
        return jsonify(1)
    return jsonify(0)


@frontend_bp.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        email = request.form['email']
    else:
        return render_template('frontend/donate.html')


@frontend_bp.route('/projects', methods=['GET'])
def projects():
    return render_template('frontend/projects.html')


@frontend_bp.route('/project-details/<project_name>', methods=['GET'])
def project_details(project_name):
    return render_template('frontend/project-details.html', project_name=project_name)
