from connectDB import ConectaBD
from sqlalchemy.orm import scoped_session
from sqlalchemy import select, update, func, null, insert
from classes.Aviao import Aviao
from models import Airplane

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
            avioes.append(Aviao(idAviao=row.id, qtAssentosEconomicos=row.qt_assentos_economicos, qtAssentosExecutivos=row.qt_assentos_executivos))
        return avioes
    
    def getAviaoById(self, idAviao):
        rAviao = self.conectaBD.getObjectById(Airplane, idAviao)
        return rAviao
    
    def updateAviaoById(self, aviao):
        self.conectaBD.updateObjectById(Airplane, aviao)
    
    def deleteAviaoByIDs(self, id):
        self.conectaBD.deleteObjectByIDs(Airplane, id)

''' aviao = Aviao(idAviao="1", qtAssentosEconomicos=3, qtAssentosExecutivos=5)
print(aviao.__repr__()) '''