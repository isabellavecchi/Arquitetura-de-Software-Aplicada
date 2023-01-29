from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, update, func, null, insert
from models import Base, User, Airport, Airplane
import logging

# print(DATABASE_URL)

class ConectaBD:
    #variaveis estaticas
    DATABASE_URL = 'postgresql+psycopg2://postgres:postgrespw@localhost:49153/universidade'
    engine = create_engine(DATABASE_URL)
    # engine = create_engine("postgresql+psycopg2://postgres:postgrespw@localhost:49153/universidade", echo=False)
        #esta ferramenta funciona para vários bancos!
        #"postgresql+driver://usuario:senha@computador/bd")
            #echo=True para mostrar as informações de log

    #constructor
    def __init__(self):
        db_session = scoped_session(sessionmaker(autocommit=False,
                                                autoflush=False,
                                                bind=ConectaBD.engine))
                                                
        Base.query = db_session.query_property()
         
        import models
        try:
            Base.metadata.create_all(bind=ConectaBD.engine)
            logging.info('TABELAS CRIADAS COM SUCESSO!!')
        except Exception as e:
            logging.info(f'{e}')
            print('{e}')
            #fazer um try catch para:  criar a base de dados apenas se ela já n tiver sido criada
            #quando já foi criada, dá erro
    
    def getConnection(self):
        try:
            Session = sessionmaker(ConectaBD.engine)
            session = Session()
            conn = ConectaBD.engine.connect()
            return session, conn
        except Exception as e:
            logging.info(f'XABUUUUU ... {e}')