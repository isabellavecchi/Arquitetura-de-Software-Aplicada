from flask import Flask,request,jsonify
from flask_restx import Api, Resource, fields
from config import DevConfig
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
import json

# from models import User
from connectDB import ConectaBD
from app import AppFunctions

flakApp = Flask(__name__)
flakApp.config.from_object(DevConfig)
db = ConectaBD()
funcApp = AppFunctions(db)

db.init_app(flakApp)
migrate = Migrate(flakApp, db)


api = Api(flakApp, doc='/docs')


signup_model=api.model(
    'SignUp',
    {
        "nome":fields.String(),
        "email":fields.String(),
        "senha":fields.String()
    }
)


login_model=api.model(
    'Login',
    {
        'nome':fields.String(),
        'senha':fields.String()
    }
)

@api.route('/cadastro')
class SignUp(Resource):
    @api.expect(signup_model)
    def post(self):
        data = request.get_json()
        hSenha = generate_password_hash(data['senha'])
        data['senha'] = hSenha
        usuario = json.loads(data)
        usuario = json.loads(funcApp.criarUsuario(usuario))

        if usuario is None:
            return jsonify({"message":f"Usuario com o nome {nome} ja existe"})

        return make_response(jsonify({"message":"User created successfuly"}),201)


@api.route('/login')
class Login(Resource):

    # @api.expect(login_model)
    def post(self):
        data=request.get_json()

        nome=data.get('nome')
        senha=data.get('senha')

        db_user=User.query.filter_by(nome=nome).first()

        if db_user and check_password_hash(db_user.senha, senha):

            access_token=create_access_token(identity=db_user.nome)
            refresh_token=create_refresh_token(identity=db_user.nome)

            return jsonify(
                {"access_token":access_token,"refresh_token":refresh_token}
            )

@api.route('/aeroportos'):
# class Aeroportos(Resource):
def post(self):
    return funcApp.listarAeroportos()
post()