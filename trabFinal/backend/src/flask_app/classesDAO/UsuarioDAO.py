# from flask_app.database.connectDB import ConectaBD
from sqlalchemy.orm import scoped_session
from sqlalchemy import select, update, func, null, insert
from classes.Usuario import Usuario
from database.models import User
import logging

class UsuarioDAO:
    #constructor
    def __init__(self, conectaBD):
        self.conectaBD = conectaBD
    
    ##### MÉTODOS DE CONTROLE DOS DADOS #####
    def confereListaUsuarios(listaUsuarios):
        listaConferida = []
        listaErrada = []
        for user in listaUsuarios:
            if hasattr(user,'nome'):
                listaConferida.append(user)
            else:
                listaErrada.append(user)
        return listaConferida #,listaErrada

    def getListaToTbUser(listaUsuarios):
        tbUsers = []
        for user in listaUsuarios:
            tbUsers.append(User(user))
        return tbUsers
    
    def getListaFromTbUser(tbUsers):
        users = []
        for rUsuario in tbUsers:
            users.append(Usuario(   idUsuario=rUsuario.id,
                                    nome=rUsuario.nome,
                                    email=rUsuario.email,
                                    senha=rUsuario.senha))
        return users
    
    def getUsuarioFromTbUser(rUsuario):
        user = Usuario( idUsuario=rUsuario.id,
                        nome=rUsuario.nome,
                        email=rUsuario.email,
                        senha=rUsuario.senha)
        return user
    
    ###################### CRUD ######################

    def addUsuario(self,user):
        # try:
            usuario = self.conectaBD.addObjectInTable(user, User)

            return usuario

        # except Exception as e:
        #     logging.info(f'XABUUUUU ... {e}')
        #     return None


    def addListUsuarios(self, users):
        try:
            self.conectaBD.addObjectsListInTable(users, User)
            return users
        
        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')


    def getAllUsers(self):
        try:
            user = self.conectaBD.getTable(User)
            return UsuarioDAO.getListaFromTbUser(user)

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')
    
    def getUserById(self, id):
        rUser = self.conectaBD.getObjectById(User, id)
        return rUser
    
    
    def updateUserById(self, usuario):
        self.conectaBD.updateObject(User, usuario)
        return usuario
    
    def deleteUsersByIDs(self, idArray):
        self.conectaBD.deleteObjectByIDs(User, idArray)


    ## CRUD extras
    
    def getAllUsersOrderedName(self):
        try:
            session = self.conectaBD.getSession()
            tbUser = session.query(User).order_by(User.nome)
            return UsuarioDAO.getListaFromTbUser(tbUser)

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')


    def getUsersByNameOrderedName(self, name):
        try:
            session = self.conectaBD.getSession()
            tbUser = session.query(User).filter(User.nome.ilike(f'%{name}%')).order_by(User.nome)
            return UsuarioDAO.getListaFromTbUser(tbUser)

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')


    def getAllUsersByNames(self, names):
        try:
            session = self.conectaBD.getSession()
            tbUser = session.query(User).filter(User.nome.in_(names)).all()
            return UsuarioDAO.getListaFromTbUser(tbUser)

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')


    def getQtdUser(self):
        try:
            session = self.conectaBD.getSession()
            qtdUsuario = session.query(User).count()
            return qtdUsuario

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')