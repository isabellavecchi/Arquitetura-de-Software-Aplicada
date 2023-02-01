from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, update, func, null, insert, text
from sqlalchemy.engine import result
from models import Base
import logging

# print(DATABASE_URL)

class ConectaBD:
    #variaveis estaticas
    DATABASE_URL = 'postgresql+psycopg2://postgres:postgrespw@localhost:49153/decolar'
    engine = create_engine(DATABASE_URL)
    # engine = create_engine("postgresql+psycopg2://postgres:postgrespw@localhost:49153/universidade", echo=False)
        #esta ferramenta funciona para vários bancos!
        #"postgresql+driver://usuario:senha@computador/bd")
            #echo=True para mostrar as warningrmações de log

    #constructor
    def __init__(self):
        db_session = scoped_session(sessionmaker(autocommit=False,
                                                autoflush=False,
                                                bind=ConectaBD.engine))
                                                
        Base.query = db_session.query_property()
         
        import models
        try:
            Base.metadata.create_all(bind=ConectaBD.engine)
            logging.warning('TABELAS CRIADAS COM SUCESSO!!')
        except Exception as e:
            logging.warning(f'{e}')
            print('{e}')
            #fazer um try catch para:  criar a base de dados apenas se ela já n tiver sido criada
            #quando já foi criada, dá erro
    
    def getSession(self):
        try:
            Session = sessionmaker(ConectaBD.engine)
            session = Session()
            return session
        except Exception as e:
            logging.warning(f'XABUUUUU ... {e}')
    
    def getConnection(self):
        try:
            conn = ConectaBD.engine.connect()
            return conn
        except Exception as e:
            logging.warning(f'XABUUUUU ... {e}')
    
    def getSessionNConnection(self):
        try:
            Session = sessionmaker(ConectaBD.engine)
            session = Session()
            conn = ConectaBD.engine.connect()
            return session, conn
        except Exception as e:
            logging.warning(f'XABUUUUU ... {e}')

    

    ###################### CRUD ######################

    def addObjectInTable(self, object, Table):
        try:
            row = Table(object)
            
            session = self.getSession()
            session.add(row)
            logging.warning(Table, ' ADICIONADO COM SUCESSO!!')
            session.commit()

            return row

        except Exception as e:
            logging.warning(f'XABUUUUU adicionando por input... ', e)
    
    def addObjectsListInTable(self, objectList, Table):
        try:
            rObjects = []
            for object in objectList:
                rObjects.append(Table(object))

            session = self.getSession()
            session.add_all(rObjects)
            session.commit()
            logging.info('USUARIES ADICIONADES COM SUCESSO!!')

            return objectList

        except Exception as e:
            logging.warning(f'XABUUUUU adicionando por input... ', e)

    def getTable(self, Table):
        try:
            session = self.getSession()
            table = session.query(Table)
            return table

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')
    
    # def getAllObjectsOrderedByColumn(self, Table, column):
    #     try:
    #         session = self.getSession()
    #         table = session.query(Table).order_by(column)
    #         return table

    #     except Exception as e:
    #         print(e)
    #         ret = {"status": str(e)}
    #         logging.info(f'XABUUUUU ... {e}')


    def getObjectById(self, Table, idObject):
        try:
            conn = self.getConnection()     
            
            s = select(Table).where(Table.id == idObject)
            rObject = conn.execute(s)
            
            result_set_as_dict = rObject.mappings().all()
            if result_set_as_dict != []:
                return result_set_as_dict[0]
            else:
                raise Exception("NENHUMA LINHA ENCONTRADA")

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info('XABUUUUU ... {',e,'}')
    
    def updateObjectById(self, Table, object):
        object = Table(object)
        session = self.getSession()
        session.query(Table).filter_by(id=object.id).update({column: getattr(object, column) for column in Table.__table__.columns.keys()})
        session.commit()
    
    def updateTable(self, Table, objectList):
        for object in objectList:
            self.updateObjectById(Table, object)
    
    def deleteObjectByIDs(self, Table, idArray):
        session = self.getSession()
        session.query(Table).filter(Table.id.in_(idArray)).delete()
        session.commit()

    # def getValuesFromQueryString(self, str):
    #     sql = text(str)
    #     # conn = self.getConnection()
    #     result_set = ConectaBD.engine.execute(str)  
    #     for r in result_set:  
    #         print(r)