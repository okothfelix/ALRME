from flask import Flask
from frontend.routes import frontend_bp
# from administrators.routes import administrators_bp


app = Flask(__name__)
app.secret_key = '70b76438bbccfd3ec8ab0ec170d4e179'

# app routes
app.register_blueprint(frontend_bp, url_prefix='/')
# app.register_blueprint(administrators_bp, url_prefix='/admin')


if __name__ == '__main__':
    app.run(debug=True, port=80)
