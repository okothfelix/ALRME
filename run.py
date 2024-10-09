from flask import Flask
from frontend.routes import frontend_bp


app = Flask(__name__)
app.register_blueprint(frontend_bp, url_prefix='/')


if __name__ == '__main__':
    app.run(debug=True)
