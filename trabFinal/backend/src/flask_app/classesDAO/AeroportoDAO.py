# from connectDB import ConectaBD
from sqlalchemy.orm import scoped_session
from sqlalchemy import select, update, func, null, insert
from classes.Aeroporto import Aeroporto
from database.models import Airport
import logging

class AeroportoDAO:
    #constructor
    def __init__(self, conectaBD):
        self.conectaBD = conectaBD
    
    def insertAeroporto(self, aeroporto):
        # try:
            return self.conectaBD.addObjectInTable(aeroporto, Airport)
            

        # except Exception as e:
        #     return None
    
    def getTbAeroporto(self):
        table = self.conectaBD.getTable(Airport)
        avioes = []
        for rAeroporto in table:
            avioes.append(Aeroporto(idAeroporto=rAeroporto.id, nome=rAeroporto.nome, estado=rAeroporto.estado, cidade=rAeroporto.cidade))
        return avioes
    
    def getAeroportoById(self, idAeroporto):
        try:
            rAeroporto = self.conectaBD.getObjectById(Airport, idAeroporto)
            return Aeroporto(idAeroporto=rAeroporto.id, nome=rAeroporto.nome, estado=rAeroporto.estado, cidade=rAeroporto.cidade)

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')
    
    def updateAeroportoById(self, aeroporto):
        self.conectaBD.updateObject(Airport, aeroporto)
    
    def deleteAeroportoByIDs(self, arrId):
        return self.conectaBD.deleteObjectByIDs(Airport, arrId)