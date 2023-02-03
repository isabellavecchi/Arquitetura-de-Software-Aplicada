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
    return funcApp.listarPassagens()




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


    #######################
    ##      INSERTS      ##
    #######################

    ## Usuario
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

    ## Aeroporto
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

    ## Voo
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

    ## Passagem
@app.route('/passagem', methods=['POST','GET'])
def passagem():
    
    if request.method == 'POST':
        passagem = request.json
        logging.info('passagem: ', passagem)
        passagem = funcApp.venderPassagem(passagem)

        if passagem is None:
            return jsonify({"msg":"passagem nao cadastrado"})
        return jsonify({"msg":"passagem cadastrado"})
    else:
        return jsonify({"msg":"passagem nao cadastrado"})
    

    ########################
    ##        GETS        ##
    ########################

    ## Aeroportos
@app.route('/listarAeroportos', methods=['GET'])
def listarAeroportos():
    return funcApp.listarPassagens()

    ## Voos
@app.route('/listarVoos', methods=['GET'])
def listarVoos():
    return funcApp.listarVoos()

    ## Voos - Disponiveis
@app.route('/listarVoosDisponiveis', methods=['GET'])
def listarVoosDisponiveis():
    return funcApp.listarVoosDisponiveis()

    ## Passagens
@app.route('/listarPassagens', methods=['GET'])
def listarPassagens():
    return funcApp.listarPassagens()
    

    #######################
    ##      DELETES      ##
    #######################

    ## Aeroporto
@app.route('/aeroportos/deletar/id', methods=['GET'])
def deletePassagem():
    id = request.json
    logging.info('id: ', voo)

    if(funcApp.deletePassagem(id)):
        return jsonify({"msg":"passagem deletada com sucesso!"})
    return jsonify({"msg":"xabu ao deletar passagem..."})
    

    #######################
    ##      UPDATES      ##
    #######################

    ## Voo
@app.route('/voos/atualiza/id', methods=['GET'])
def updateVoo():
    
    id = request.json
    logging.info('id: ', voo)
    voo = funcApp.updateVoo(id)

    if passagem is None:
        return jsonify({"msg":"erro ao atualizar passagem..."})
    return jsonify({"msg":"passagem atualizada com sucesso!!"})


if __name__ == '__main__':
    app.run(debug=True, port=5000)