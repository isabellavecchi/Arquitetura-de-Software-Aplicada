from connectDB import ConectaBD
from sqlalchemy.orm import scoped_session
from sqlalchemy import select, update, func, null, insert
from classes.Voo import Voo
from models import Flight
import logging

class VooDAO:
    #constructor
    def __init__(self, conectaBD):
        self.conectaBD = conectaBD
    
    def insertVoo(self, voo):
        self.conectaBD.addObjectInTable(voo, Flight)
        return voo
    
    def getTbVoo(self):
        table = self.conectaBD.getTable(Flight)
        voos = []
        for rVoo in table:
            voos.append(Voo(idVoo=rVoo.id, lugaresDisponiveis=rVoo.qt_lugares_disponiveis, dataDeSaida=rVoo.data_saida, idAeroportoSaida=rVoo.id_aeroporto_saida, dataDeChegada=rVoo.data_chegada, idAeroportoChegada=rVoo.id_aeroporto_chegada, preco=rVoo.preco))
        return voos
    
    # def getTbVooOrderByPreco(self):
    #     try:
    #         session = self.conectaBD.getSession()
    #         table = session.query(Flight).order_by(Flight.preco)
    #         voos = []
    #         for rVoo in table:
    #             voos.append(Voo(idVoo=rVoo.id, lugaresDisponiveis=rVoo.qt_lugares_disponiveis, dataDeSaida=rVoo.data_saida, idAeroportoSaida=rVoo.id_aeroporto_saida, dataDeChegada=rVoo.data_chegada, idAeroportoChegada=rVoo.id_aeroporto_chegada, preco=rVoo.preco))
    #         return voos

        # except Exception as e:
        #     print(e)
        #     ret = {"status": str(e)}
        #     logging.info(f'XABUUUUU ... {e}')
    
    def getVooById(self, idVoo):
        try:
            rVoo = self.conectaBD.getObjectById(Flight, idVoo)
            return Voo(idVoo=rVoo.id, lugaresDisponiveis=rVoo.qt_lugares_disponiveis, dataDeSaida=rVoo.data_saida, idAeroportoSaida=rVoo.id_aeroporto_saida, dataDeChegada=rVoo.data_chegada, idAeroportoChegada=rVoo.id_aeroporto_chegada, preco=rVoo.preco)

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... ', e)
    
    def updateVooById(self, voo):
        self.conectaBD.updateObjectById(Flight, voo)
    
    def deleteVooByIDs(self, id):
        self.conectaBD.deleteObjectByIDs(Flight, id)
