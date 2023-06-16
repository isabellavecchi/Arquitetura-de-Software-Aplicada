#import database_utils
from flask import Blueprint, request, json, jsonify
from sqlalchemy import create_engine, select, update, func, null, insert
from sqlalchemy.orm.session import sessionmaker
import connectDB
from studentDAO import EstudanteDAO
from student import Estudante
from models import TbEstudante

conectaBD = None

urls_blueprint = Blueprint('urls', __name__,)

@urls_blueprint.route('/')
def index():
    return 'urls index route'

@urls_blueprint.route('/create_tables', methods = ['GET'])
def create_database():
    try:
        conectaBD.init_db()
        ret = {"status": "Tables are created!!"}

    except Exception as e:
        print(e)
        ret = {"status": "Tables are not created!!"}    
    return ret    

@urls_blueprint.route('/estudantes', methods = ['POST'])
def add_estudante():
    try:
        req_data = request.get_json()
        estudante = Estudante(nome=req_data['nome'], endereco=req_data['endereco'], email=req_data['email'])

        #database.add_estudante() --> sem o JSON
        ret = database.addEstudante(estudante)
        print(estudante)
        #ret = {"status": "User has been added"}

    except Exception as e:
        print(e)
        ret = {"status": "Student are not registered!!"}    
    return ret    
    

@urls_blueprint.route('/estudantes', methods = ['GET'])
def getAllStudents():
    database.getAllStudents()
    ret = {"status": "List of students"}
    return ret


''' student1 = Estudante(nome="estudante Um", endereco="Rua 1", email="estudante1@ufu.br")
student2 = Estudante(nome="estudante Dois", endereco="Rua 2", email="estudante2@ufu.br")
alunos = []
alunos.append(student1)
alunos.append(student2)
addListEstudantes(alunos)

addEstudanteInputs('Isabella', 'Av. João XXIII, 768', 'isabellavecchi@ufu.br')

student4 = Estudante(nome="estudante Quatro", endereco="Rua 4", email="estudante4@ufu.br")
addEstudante(student4)

student5 = TbEstudante(Estudante(nome="estudante Cinco", endereco="Rua 5", email="estudante5@ufu.br"))
student6 = TbEstudante(Estudante(nome="estudante Seis", endereco="Rua 6", email="estudante6@ufu.br"))
alunos = []
alunos.append(student5)
alunos.append(student6)
addListEstudantes(alunos)


alunos = getAllStudents()
for aluno in alunos:
    print(aluno) '''








#ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
#>>> session.add(ed_user)
        # Session = sessionmaker(self.db)
        # self.session = Session()     

            # query = (
            #         insert(Envios_Lembretes).
            #         values(
            #             id_lembrete = envio_lembrete.id_lembrete,
            #             id_estudante = envio_lembrete.id_estudante,
            #             lembrete = envio_lembrete.lembrete,
            #             data_para_envio = envio_lembrete.data_para_envio,
            #             data_enviado = None,
            #             meio_envio = envio_lembrete.meio_envio,
            #             criado_em = datetime.now()
            #             )
            # )
            # conn = self.db.connect()
            # result = conn.execute(query)

            # self.session.commit()
            # logging.debug("ATUALIZANDO ADCIONANDO UM NOVO ENVIOS_LEMBRETES")
    
