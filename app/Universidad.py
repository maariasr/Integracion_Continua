from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/universidad'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instanciamos db
db = SQLAlchemy(app)

# Instanciamos marshmallow
ma = Marshmallow(app)

# Creacion tabla curso
class Curso(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    creditos = db.Column(db.Integer)

    def __init_(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos

# Definción del esquema
class CursoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'creditos')

# Una sola respuesta
curso_schema = CursoSchema()

# Varias respuestas
cursos_schema = CursoSchema(many = True)

# Ruta Curso
@app.route('/curso', methods=['GET'])

def get_cursos():
    all_cursos = Curso.query.all()
    result = cursos_schema.dump(all_cursos)
    return jsonify(result)

# Mensaje de bienvenida
@app.route('/', methods=['GET'])

def index():
    return jsonify({'Mensaje':'Bienvenido!'})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 4000, debug = True)