from connectDB import ConectaBD
from sqlalchemy.orm import scoped_session
from sqlalchemy import select, update, func, null, insert
from classes.Passagem import Passagem
from models import Booking
import logging

class PassagemDAO:
    #constructor
    def __init__(self, conectaBD):
        self.conectaBD = conectaBD
    
    def insertPassagem(self, passagem):
        return self.conectaBD.addObjectInTable(passagem, Booking)
    
    def getTbPassagem(self):
        table = self.conectaBD.getTable(Booking)
        passagens = []
        for rPassagem in table:
            passagens.append(Passagem(idPassagem=rPassagem.id, idVoo=rPassagem.id_voo, nomeComprador=rPassagem.nome_comprador, cpfComprador=rPassagem.cpf_comprador))
        return passagens
    
    def getPassagemById(self, idPassagem):
        try:
            rPassagem = self.conectaBD.getObjectById(Booking, idPassagem)
            return Passagem(idPassagem=rPassagem.id, idVoo=rPassagem.id_voo, nomeComprador=rPassagem.nome_comprador, cpfComprador=rPassagem.cpf_comprador)

        except Exception as e:
            print(e)
            ret = {"status": str(e)}
            logging.info(f'XABUUUUU ... {e}')
    
    def updatePassagemById(self, passagem):
        self.conectaBD.updateObject(Booking, passagem)
    
    def deletePassagemByIDs(self, arrId):
        self.conectaBD.deleteObjectByIDs(Booking, arrId)
    
    # def listarPassagens(self):
    #     self.conectaBD.getValuesFromQueryString('Select * from tb_passagem;')