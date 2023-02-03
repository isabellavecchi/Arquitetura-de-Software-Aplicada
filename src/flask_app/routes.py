from flask_restx import Api, Resource,Namespace,fields
# from models import User
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import JWTManager,create_access_token,create_refresh_token,jwt_required
from flask import Flask,request,jsonify,make_response, render_template, abort
from json import dumps

# from config import DevConfig
# from flask_migrate import Migrate
import json, logging

# from models import User
from connectDB import ConectaBD
from app import AppFunctions

# app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

''' TESTE '''
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET','POST'])
def notas():
    
    if request.method == 'POST':
        print('###########routes')
        objeto = request.json
        print('objeto: ', objeto)

        objeto = funcApp.criarVoo(objeto)
        print('###########depois de criar o objeto')
        # print('objeto: ', objeto)

        if objeto is None:
            return jsonify({"msg":"objeto nao cadastrado"})
        return jsonify({"msg":"objeto cadastrado"})
    else:
        return jsonify({"msg":"objeto nao cadastrado"})



''' FIM DA AREA DE TESTE '''

# flakApp = Flask(__name__)
# flakApp.config.from_object(DevConfig)
# app = Api(flakApp) #, doc='/docs')

db = ConectaBD()
funcApp = AppFunctions(db)


# db.init_app(flakApp)
# migrate = Migrate(flakApp, db)



# signup_model=app.model(
#     'SignUp',
#     {
#         "nome":fields.String(),
#         "email":fields.String(),
#         "senha":fields.String()
#     }
# )


# login_model=app.model(
#     'Login',
#     {
#         'nome':fields.String(),
#         'senha':fields.String()
#     }
# )

# @app.route('/cadastro')
# # class SignUp(Resource):
#     # @app.expect(signup_model)
# def cadastro(self):
#     data = request.get_json()
#     hSenha = generate_password_hash(data['senha'])
#     data['senha'] = hSenha
#     usuario = json.loads(data)
#     usuario = json.loads(funcApp.criarUsuario(usuario))

#     if usuario is None:
#         return jsonify({"message":f"Usuario com o nome {nome} ja existe"})

#     return jsonify({"message":"User created successfuly"})


# @app.route('/login')
# class Login(Resource):

#     # @app.expect(login_model)
#     def post(self):
#         data=request.get_json()

#         nome=data.get('nome')
#         senha=data.get('senha')

#         db_user=User.query.filter_by(nome=nome).first()

#         if db_user and check_password_hash(db_user.senha, senha):

#             access_token=create_access_token(identity=db_user.nome)
#             refresh_token=create_refresh_token(identity=db_user.nome)

#             return jsonify(
#                 {"access_token":access_token,"refresh_token":refresh_token}
#             )

@app.route('/usuario', methods=['POST','GET'])
def usuario():
    
    if request.method == 'POST':
        usuario = request.json
        logging.info('usuario: ', usuario)
        usuario = funcApp.criarUsuario(usuario)

        if usuario is None:
            return jsonify({"msg":"usuario nao cadastrado"})
        return jsonify({"msg":"usuario cadastrado"})
    else:
        return jsonify({"msg":"usuario nao cadastrado"})


@app.route('/aeroporto', methods=['POST','GET'])
def aeroporto():
    
    if request.method == 'POST':

        aeroporto = request.json
        logging.info('aeroporto: ', aeroporto)
        aeroporto = funcApp.criarAeroporto(aeroporto)

        if aeroporto is None:
            return jsonify({"msg":"aeroporto nao cadastrado"})
        return jsonify({"msg":"aeroporto cadastrado"})
    else:
        return jsonify({"msg":"aeroporto nao cadastrado"})


@app.route('/voo', methods=['POST','GET'])
def voo():
    
    if request.method == 'POST':
    
        voo = request.json
        logging.info('voo: ', voo)
        voo = funcApp.criarVoo(voo)

        if voo is None:
            return jsonify({"msg":"voo nao cadastrado"})
        return jsonify({"msg":"voo cadastrado"})
    else:
        return jsonify({"msg":"voo nao cadastrado"})
    
# @app.route('/aeroportos'):
# # class Aeroportos(Resource):
# def post(self):
#     return funcApp.listarAeroportos()
# post()

if __name__ == '__main__':
    app.run(debug=True, port=5000)