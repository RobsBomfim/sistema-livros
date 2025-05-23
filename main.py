from flask import Flask
from app.controller.controller_livros import consulta_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Registrar Blueprints
app.register_blueprint(consulta_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
