# from connectDB import ConectaBD
from sqlalchemy.orm import scoped_session
from sqlalchemy import select, update, func, null, insert
from classes.Aviao import Aviao
from database.models import Airplane
import logging

class AviaoDAO:
    #constructor
    def __init__(self, conectaBD):
        self.conectaBD = conectaBD
    
    def insertAviao(self, aviao):
        self.conectaBD.addObjectInTable(aviao, Airplane)
        return aviao
    
    def getTbAviao(self):
        table = self.conectaBD.getTable(Airplane)
        avioes = []
        for row in table:
            avioes.append(Aviao(idAviao=row.id, qtTotalAssentos=row.qt_total_assentos))
        return avioes
    
    def getAviaoById(self, idAviao):
        try:
            rAviao = self.conectaBD.getObjectById(Airplane, idAviao)
            return Aviao(idAviao=rAviao.id, qtTotalAssentos=rAviao.qt_total_assentos)

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')
    
    def updateAviaoById(self, aviao):
        self.conectaBD.updateObject(Airplane, aviao)
    
    def deleteAviaoByIDs(self, id):
        self.conectaBD.deleteObjectByIDs(Airplane, id)

''' aviao = Aviao(idAviao="1", qtAssentosEconomicos=3, qtAssentosExecutivos=5)
print(aviao.__repr__()) '''