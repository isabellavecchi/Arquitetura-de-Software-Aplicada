
from connectDB import ConectaBD
from sqlalchemy.orm import scoped_session
from sqlalchemy import select, update, func, null, insert
from connectDB import ConectaBD
from student import Estudante
from models import TbEstudante
import logging

class EstudanteDAO:
    #constructor
    def __init__(self, conectaBD):
        self.conectaBD = conectaBD
    
    # MÉTODOS DE CONTROLE DOS DADOS
    def confereListaEstudantes(listaEstudantes):
        listaConferida = []
        listaErrada = []
        for estudante in listaEstudantes:
            if hasattr(estudante,'nome'):
                listaConferida.append(estudante)
            else:
                listaErrada.append(estudante)
        return listaConferida,listaErrada

    def getListaToTbEstudante(listaEstudantes):
        tbEstudantes = []
        for estudante in listaEstudantes:
            tbEstudantes.append(TbEstudante(estudante))
        return tbEstudantes
    
    def getListaFromTbEstudante(tbEstudantes):
        estudantes = []
        for rEstudante in tbEstudantes:
            estudantes.append(Estudante(matricula=rEstudante.getMatricula(),
                                        nome=rEstudante.getNome(),
                                        cpf=rEstudante.getCPF(),
                                        endereco=rEstudante.getEndereco(),
                                        email=rEstudante.getEmail()))
        return estudantes
    
    def getEstudanteFromTbEstudante(rEstudante):
        estudante = Estudante(  matricula=int(rEstudante.getMatricula()),
                                nome=rEstudante.getNome(),
                                cpf=rEstudante.getCPF(),
                                endereco=rEstudante.getEndereco(),
                                email=rEstudante.getEmail())
        return estudante
    
    # MÉTODOS DE INSERT NO BANCO
    def addEstudanteInputs(self, _nome, _cpf, _endereco, _email):
        try:
            estudante = Estudante(nome=_nome, cpf=_cpf, endereco=_endereco, email=_email)
            rEstudante = TbEstudante(estudante)
            
            session, conn = self.conectaBD.getConnection()
            session.add(rEstudante)
            logging.info('ESTUDANTE ADICIONADO COM SUCESSO!!')
            session.commit()

            return estudante

        except Exception as e:
            logging.info(f'XABUUUUU adicionando por input... {e}')

    def addEstudante(self,estudante):
        try:
            rEstudante = TbEstudante(estudante)

            session, conn = self.conectaBD.getConnection()
            session.add(rEstudante)
            logging.info('ESTUDANTE ADICIONADO COM SUCESSO!!')
            session.commit()

            return rEstudante

        except Exception as e:
            logging.info(f'XABUUUUU ... {e}')

    def addEstudanteJson(self, json_Estudante):
        try:
            estudante = Estudante(nome=json_Estudante['nome'], cpf=json_Estudante['cpf'], endereco = json_Estudante['endereco'], email = json_Estudante['email'])
            rEstudante = TbEstudante(estudante)

            session, conn = self.conectaBD.getConnection()
            session.add(rEstudante)
            session.commit()
            logging.info('ESTUDANTE ADICIONADO COM SUCESSO!!')

            return estudante
        
        except Exception as e:
            print(e)
            logging.info(f'XABUUUUU ... {e}')


    def addListEstudantes(self, estudantes):
        try:
            if (type(estudantes[0]) is Estudante):
                estudantes = EstudanteDAO.confereListaEstudantes(estudantes)
                tbEstudantes = EstudanteDAO.getListaToTbEstudante(estudantes)
                estudantes = tbEstudantes

            ## SEGURANÇA: decidi nao deixar adicionar dados sem antes passar pelos filtros da classe Estudante
            # elif (type(estudantes[0]) is not TbEstudante):

            else:
                raise Exception ("Tipo de Objeto nao suportado!")

            session, conn = self.conectaBD.getConnection()
            session.add_all(estudantes)
            session.commit()
            logging.info('ESTUDANTES ADICIONADES COM SUCESSO!!')

            return estudantes
        
        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')


    # MÉTODOS DE SELECT NO BANCO
    def getAllStudents(self):
        try:
            session, conn = self.conectaBD.getConnection()
            tbEstudante = session.query(TbEstudante)
            return EstudanteDAO.getListaFromTbEstudante(tbEstudante)

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')


    def getStudentByCPF(self, cpf):
        cpf = Estudante.getNumsFromCPF(cpf)
        try:
            if not (Estudante.validaCPF(cpf=cpf)):
                raise Exception("ALGUM CARACTERE DE [CPF] EH INVALIDO!!!")

            session, conn = self.conectaBD.getConnection()
            rEstudante = session.query(TbEstudante).filter(TbEstudante.cpf.ilike(f'{cpf}')).first()
            # estudante = EstudanteDAO.getEstudanteFromTbEstudante(rEstudante)
            return rEstudante

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')


    def getAllStudentsOrderedName(self):
        try:
            session, conn = self.conectaBD.getConnection()
            tbEstudante = session.query(TbEstudante).order_by(TbEstudante.nome)
            return EstudanteDAO.getListaFromTbEstudante(tbEstudante)

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')


    def getAllStudentsOrderedRegister(self):
        try:
            session, conn = self.conectaBD.getConnection()
            tbEstudante = session.query(TbEstudante).order_by(TbEstudante.matricula)
            return EstudanteDAO.getListaFromTbEstudante(tbEstudante)

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')


    def getStudentsByNameOrderedName(self, name):
        try:
            if  not (name == "" or Estudante.validaNome(name)):
                raise Exception("ALGUM CARACTERE DE [NOME] EH INVALIDO!!!")
            session, conn = self.conectaBD.getConnection()
            tbEstudante = session.query(TbEstudante).filter(TbEstudante.nome.ilike(f'%{name}%')).order_by(TbEstudante.nome)
            return EstudanteDAO.getListaFromTbEstudante(tbEstudante)

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')


    def getStudentsByNameOrderedRegister(self, name):
        try:
            if  not (name == "" or Estudante.validaNome(name)):
                raise Exception("ALGUM CARACTERE DE [NOME] EH INVALIDO!!!")
            session, conn = self.conectaBD.getConnection()
            tbEstudante = session.query(TbEstudante).filter(TbEstudante.nome.ilike(f'%{name}%')).order_by(TbEstudante.matricula)
            return EstudanteDAO.getListaFromTbEstudante(tbEstudante)

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')


    def getAllStudentsByName(self, name):
        try:
            if not (Estudante.validaNome(name)):
                raise Exception("ALGUM CARACTERE DE [NOME] EH INVALIDO!!!")
            session, conn = self.conectaBD.getConnection()
            tbEstudante = session.query(TbEstudante).filter(TbEstudante.nome.ilike(f'%{name}%')).all()
            return EstudanteDAO.getListaFromTbEstudante(tbEstudante)

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')


    def getAllStudentsByNames(self, names):
        try:
            for name in names:
                if not (Estudante.validaNome(name)):
                    raise Exception("ALGUM CARACTERE DE [NOME] EH INVALIDO!!!")
            session, conn = self.conectaBD.getConnection()
            tbEstudante = session.query(TbEstudante).filter(TbEstudante.nome.in_(names)).all()
            return EstudanteDAO.getListaFromTbEstudante(tbEstudante)

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')


    def getQtdStudent(self):
        try:
            session, conn = self.conectaBD.getConnection()
            qtdEstudante = session.query(TbEstudante).count()
            return qtdEstudante

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')
    
    def updateStudent(self, cpf, newEstudante):
        rEstudante = self.getStudentByCPF(cpf)
        if(type(newEstudante) is Estudante):
            pass
        elif(type(newEstudante) is TbEstudante):
            newEstudante = EstudanteDAO.getEstudanteFromTbEstudante(newEstudante)
        else:
            raise Exception("TIPO DE OBJETO NAO SUPORTADO!!!")
        rEstudante.setNome(newEstudante.getNome())
        rEstudante.setCPF(newEstudante.getCPF())
        rEstudante.setEndereco(newEstudante.getEndereco())
        rEstudante.setEmail(newEstudante.getEmail())

        


# conectaBD = ConectaBD()
# estudanteDAO = EstudanteDAO(conectaBD)

# restudante = estudanteDAO.getStudentByCPF("123.123.123-12")
# if(restudante is not None):
#     print("encontrou")
#     estudante = EstudanteDAO.getEstudanteFromTbEstudante(restudante)
#     estudante.printa()
# else:
#     print("nao encontrou")
# aluno = estudanteDAO.getStudentByRegister(2)
# print(type(aluno))
''' rstudent1 = Estudante(nome="estudante Dois", cpf="12312312311", endereco="Rua 2", email="estudante2@ufu.br")
print("criou")
print(rstudent1)
estudanteDAO.addEstudante(rstudent1) '''
#addEstudante
''' alunos = []
print("antes do 1")
student1 = Estudante(nome="estudante Um", endereco="Rua 1", email="estudante1@ufu.br")
student1.printa() 
alunos.append(student1)
print("antes do 2")
student2 = Estudante(nome="estudante Dois", endereco="Rua 2", email="estudante2@ufu.br")
# print(student2.__repr__)
print("depois do 2 e antes de add na lista")
alunos.append(student2)
estudanteDAO.addListEstudantes(alunos)
print("depois de add a lista tb")

estudanteDAO.addEstudanteInputs('Isabella', 'Av. J@oão XXIII, 768', 'isabellavecchi@ufu.br')
estudanteDAO.addEstudanteInputs('Isabella', 'Av. João XXIII, 768', 'isabellavecchi@ufu.br')

student4 = Estudante(nome="estudante Quatro", endereco="Rua 4", email="estudant)e4@ufu.br")
estudanteDAO.addEstudante(student4)

student4 = Estudante(nome="estudante Quatro", endereco="Rua 4", email="estudante4@ufu.br")
estudanteDAO.addEstudante(student4)

student5 = TbEstudante(Estudante(nome="estudante Cinco", endereco="Rua 5", email="estudante5@ufu.br"))
student6 = TbEstudante(Estudante(nome="estudante Seis", endereco="Rua 6", email="estudante6@ufu.br"))
alunos = []
alunos.append(student5)
alunos.append(student6)
estudanteDAO.addListEstudantes(alunos)

 '''
# alunos = estudanteDAO.getAllStudents()
# alunos = estudanteDAO.getAllStudentsOrderedName()
# alunos = estudanteDAO.getAllStudentsOrderedRegister()
# alunos = estudanteDAO.getStudentsByNameOrderedName("")
# alunos = estudanteDAO.getAllStudentsByNames(["estudante Dois","estudante Quatro"])


# for aluno in alunos:
#     print(aluno.__repr__())

# qtd = estudanteDAO.getQtdStudent()
# print(qtd)