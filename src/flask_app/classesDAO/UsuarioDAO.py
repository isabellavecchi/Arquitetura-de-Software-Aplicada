from connectDB import ConectaBD
from sqlalchemy.orm import scoped_session
from sqlalchemy import select, update, func, null, insert
from User import Usuario
from models import TbUsuario
import logging

class UsuarioDAO:
    #constructor
    def __init__(self, conectaBD):
        self.conectaBD = conectaBD
    
    # MÉTODOS DE CONTROLE DOS DADOS
    def confereListaUsuarios(listaUsuarios):
        listaConferida = []
        listaErrada = []
        for user in listaUsuarios:
            if hasattr(user,'nome'):
                listaConferida.append(user)
            else:
                listaErrada.append(user)
        return listaConferida #,listaErrada

    def getListaToTbUsuario(listaUsuarios):
        tbUsuarios = []
        for user in listaUsuarios:
            tbUsuarios.append(TbUsuario(user))
        return tbUsuarios
    
    def getListaFromTbUsuario(tbUsuarios):
        users = []
        for rUsuario in tbUsuarios:
            users.append(Usuario(   nome=rUsuario.getNome(),
                                    cpf=rUsuario.getCPF(),
                                    endereco=rUsuario.getEndereco(),
                                    email=rUsuario.getEmail()))
        return users
    
    def getUsuarioFromTbUsuario(rUsuario):
        user = Usuario( nome=rUsuario.getNome(),
                        cpf=rUsuario.getCPF(),
                        endereco=rUsuario.getEndereco(),
                        email=rUsuario.getEmail())
        return user
    
    # MÉTODOS DE INSERT NO BANCO
    def addUsuarioInputs(self, _nome, _cpf, _endereco, _email):
        try:
            user = Usuario(nome=_nome, cpf=_cpf, endereco=_endereco, email=_email)
            rUsuario = TbUsuario(user)
            
            session, conn = self.conectaBD.getConnection()
            session.add(rUsuario)
            logging.info('Usuario ADICIONADO COM SUCESSO!!')
            session.commit()

            return user

        except Exception as e:
            logging.info(f'XABUUUUU adicionando por input... {e}')

    def addUsuario(self,user):
        try:
            rUsuario = TbUsuario(user)

            session, conn = self.conectaBD.getConnection()
            session.add(rUsuario)
            logging.info('Usuario ADICIONADO COM SUCESSO!!')
            session.commit()

            return rUsuario

        except Exception as e:
            logging.info(f'XABUUUUU ... {e}')

    def addUsuarioJson(self, json_usuario):
        try:
            user = Usuario(nome=json_usuario['nome'], cpf=json_usuario['cpf'], endereco = json_usuario['endereco'], email = json_usuario['email'])
            rUsuario = TbUsuario(user)

            session, conn = self.conectaBD.getConnection()
            session.add(rUsuario)
            session.commit()
            logging.info('Usuario ADICIONADO COM SUCESSO!!')

            return user
        
        except Exception as e:
            print(e)
            logging.info(f'XABUUUUU ... {e}')


    def addListUsuarios(self, users):
        try:
            if (type(users[0]) is Usuario):
                users = UsuarioDAO.confereListaUsuarios(users)
                tbUsuarios = UsuarioDAO.getListaToTbUsuario(users)
                users = tbUsuarios

            ## SEGURANÇA: decidi nao deixar adicionar dados sem antes passar pelos filtros da classe Usuario
            # elif (type(Usuarios[0]) is not TbUsuario):

            else:
                raise Exception ("Tipo de Objeto nao suportado!")

            session, conn = self.conectaBD.getConnection()
            session.add_all(users)
            session.commit()
            logging.info('USUARIES ADICIONADES COM SUCESSO!!')

            return users
        
        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')


    # MÉTODOS DE SELECT NO BANCO
    def getAllUsers(self):
        try:
            session, conn = self.conectaBD.getConnection()
            tbUsuario = session.query(TbUsuario)
            return UsuarioDAO.getListaFromTbUsuario(tbUsuario)

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')


    def getUserByCPF(self, cpf):
        cpf = Usuario.getNumsFromCPF(cpf)
        try:
            if not (Usuario.validaCPF(cpf=cpf)):
                raise Exception("ALGUM CARACTERE DE [CPF] EH INVALIDO!!!")

            session, conn = self.conectaBD.getConnection()
            rUsuario = session.query(TbUsuario).filter(TbUsuario.cpf.ilike(f'{cpf}')).first()
            # Usuario = UsuarioDAO.getUsuarioFromTbUsuario(rUsuario)
            return rUsuario

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')


    def getAllUsersOrderedName(self):
        try:
            session, conn = self.conectaBD.getConnection()
            tbUsuario = session.query(TbUsuario).order_by(TbUsuario.nome)
            return UsuarioDAO.getListaFromTbUsuario(tbUsuario)

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')


    def getAllUsersOrderedRegister(self):
        try:
            session, conn = self.conectaBD.getConnection()
            tbUsuario = session.query(TbUsuario).order_by(TbUsuario.matricula)
            return UsuarioDAO.getListaFromTbUsuario(tbUsuario)

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')


    def getUsersByNameOrderedName(self, name):
        try:
            if  not (name == "" or Usuario.validaNome(name)):
                raise Exception("ALGUM CARACTERE DE [NOME] EH INVALIDO!!!")
            session, conn = self.conectaBD.getConnection()
            tbUsuario = session.query(TbUsuario).filter(TbUsuario.nome.ilike(f'%{name}%')).order_by(TbUsuario.nome)
            return UsuarioDAO.getListaFromTbUsuario(tbUsuario)

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')


    def getUsersByNameOrderedRegister(self, name):
        try:
            if  not (name == "" or Usuario.validaNome(name)):
                raise Exception("ALGUM CARACTERE DE [NOME] EH INVALIDO!!!")
            session, conn = self.conectaBD.getConnection()
            tbUsuario = session.query(TbUsuario).filter(TbUsuario.nome.ilike(f'%{name}%')).order_by(TbUsuario.matricula)
            return UsuarioDAO.getListaFromTbUsuario(tbUsuario)

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')


    def getAllUsersByName(self, name):
        try:
            if not (Usuario.validaNome(name)):
                raise Exception("ALGUM CARACTERE DE [NOME] EH INVALIDO!!!")
            session, conn = self.conectaBD.getConnection()
            tbUsuario = session.query(TbUsuario).filter(TbUsuario.nome.ilike(f'%{name}%')).all()
            return UsuarioDAO.getListaFromTbUsuario(tbUsuario)

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')


    def getAllUsersByNames(self, names):
        try:
            for name in names:
                if not (Usuario.validaNome(name)):
                    raise Exception("ALGUM CARACTERE DE [NOME] EH INVALIDO!!!")
            session, conn = self.conectaBD.getConnection()
            tbUsuario = session.query(TbUsuario).filter(TbUsuario.nome.in_(names)).all()
            return UsuarioDAO.getListaFromTbUsuario(tbUsuario)

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')


    def getQtdUser(self):
        try:
            session, conn = self.conectaBD.getConnection()
            qtdUsuario = session.query(TbUsuario).count()
            return qtdUsuario

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')
    
    def updateUser(self, cpf, newUsuario):
        rUsuario = self.getUserByCPF(cpf)
        if(type(newUsuario) is Usuario):
            pass
        elif(type(newUsuario) is TbUsuario):
            newUsuario = UsuarioDAO.getUsuarioFromTbUsuario(newUsuario)
        else:
            raise Exception("TIPO DE OBJETO NAO SUPORTADO!!!")
        rUsuario.setNome(newUsuario.getNome())
        rUsuario.setCPF(newUsuario.getCPF())
        rUsuario.setEndereco(newUsuario.getEndereco())
        rUsuario.setEmail(newUsuario.getEmail())

        


# conectaBD = ConectaBD()
# UsuarioDAO = UsuarioDAO(conectaBD)

# rUsuario = UsuarioDAO.getUserByCPF("123.123.123-12")
# if(rUsuario is not None):
#     print("encontrou")
#     Usuario = UsuarioDAO.getUsuarioFromTbUsuario(rUsuario)
#     Usuario.printa()
# else:
#     print("nao encontrou")
# aluno = UsuarioDAO.getUserByRegister(2)
# print(type(aluno))
''' rUser1 = Usuario(nome="Usuario Dois", cpf="12312312311", endereco="Rua 2", email="Usuario2@ufu.br")
print("criou")
print(rUser1)
UsuarioDAO.addUsuario(rUser1) '''
#addUsuario
''' alunos = []
print("antes do 1")
User1 = Usuario(nome="Usuario Um", endereco="Rua 1", email="Usuario1@ufu.br")
User1.printa() 
alunos.append(User1)
print("antes do 2")
User2 = Usuario(nome="Usuario Dois", endereco="Rua 2", email="Usuario2@ufu.br")
# print(User2.__repr__)
print("depois do 2 e antes de add na lista")
alunos.append(User2)
UsuarioDAO.addListUsuarios(alunos)
print("depois de add a lista tb")

UsuarioDAO.addUsuarioInputs('Isabella', 'Av. J@oão XXIII, 768', 'isabellavecchi@ufu.br')
UsuarioDAO.addUsuarioInputs('Isabella', 'Av. João XXIII, 768', 'isabellavecchi@ufu.br')

User4 = Usuario(nome="Usuario Quatro", endereco="Rua 4", email="estudant)e4@ufu.br")
UsuarioDAO.addUsuario(User4)

User4 = Usuario(nome="Usuario Quatro", endereco="Rua 4", email="Usuario4@ufu.br")
UsuarioDAO.addUsuario(User4)

User5 = TbUsuario(Usuario(nome="Usuario Cinco", endereco="Rua 5", email="Usuario5@ufu.br"))
User6 = TbUsuario(Usuario(nome="Usuario Seis", endereco="Rua 6", email="Usuario6@ufu.br"))
alunos = []
alunos.append(User5)
alunos.append(User6)
UsuarioDAO.addListUsuarios(alunos)

 '''
# alunos = UsuarioDAO.getAllUsers()
# alunos = UsuarioDAO.getAllUsersOrderedName()
# alunos = UsuarioDAO.getAllUsersOrderedRegister()
# alunos = UsuarioDAO.getUsersByNameOrderedName("")
# alunos = UsuarioDAO.getAllUsersByNames(["Usuario Dois","Usuario Quatro"])


# for aluno in alunos:
#     print(aluno.__repr__())

# qtd = UsuarioDAO.getQtdUser()
# print(qtd)