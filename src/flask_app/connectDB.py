from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, update, func, null, insert
# from models import Base, User, Airport, Airplane, Flight, Booking
from models import Base, Airplane
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
            logging.warning(f'XABUUUUU adicionando por input... {e}')
    
    def getTable(self, Table):
        try:
            session = self.getSession()
            table = session.query(Table)
            return table

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')

    def getObjectById(self, Table, idObject):
        conn = self.getConnection()     
        
        s = select(Table).where(Table.id == idObject)
        rObject = conn.execute(s)
        
        result_set_as_dict = rObject.mappings().all()
        return result_set_as_dict
        # for row in res:
        #     logging.info(f"{row['nome']}")        
        #     print(row['nome'])
    
    def updateObjectById(self, Table, object):
        object = Table(object)
        session = self.getSession()
        session.query(Table).filter_by(id=object.id).update({column: getattr(object, column) for column in Table.__table__.columns.keys()})
        session.commit()
    
    def updateTable(self, Table, objectList):
        for object in objectList:
            self.updateObjectById(Table, object)
    
    def deleteObjectByIDs(self, Table, id):
        session = self.getSession()
        session.query(Table).filter(Table.id.in_(id)).delete()
        session.commit()