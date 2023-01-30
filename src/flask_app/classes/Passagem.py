import json
import re
import logging

from Aeroporto import Aeroporto
from Aviao import Aviao
from Voo import Voo
from Usuario import Usuario

class Passagem:
    #construtor
    def __init__(self, idPassagem=None, idVoo=None, dataDeCompra=None, idUsuario=None):
        try:
            self.idPassagem = idPassagem
            self.idVoo = idVoo
            self.dataDeCompra = dataDeCompra
            self.idUsuario = idUsuario
            
        except Exception as e:
            logging.info(f'{e}')
            print(e)
            self = None

        logging.info('DADOS DE Passagem DENTRO DOS PADROES!!')

    def __iter__(self): #cria dicionario
        yield from{
            "idPassagem": self.idPassagem,
            "idVoo": self.idVoo,
            "dataDeCompra": self.dataDeCompra,
            "idUsuario": self.idUsuario
        }.items()
    
    #envia uma estrutura em formato de dicionário (dict interage com o método iter)
    def __str__(self):
        return json.dumps(dict(self), ensure_ascii = False)
    
    #usado no momento que dou o print
    def __repr__(self):
        return 'Passagem: %s\nidUsuario: %s\nidVoo: %s\ndataDeCompra: %s\n' % (self.getId(), self.getIdUsuario().getNome(), self.getIdVoo(), self.getDataDeCompra())
    
    def printa(self):
        print(self.__repr__())

    # def from_json(json_file):
    #     return Passagem(json.load(dict(json_file), ensure_ascii = False))

    def to_json(self):
        return self.__str__()


    #VALIDACOES
    # GETTERS AND SETTERS

    def setId(self,idPassagem):
        self.idPassagem = idPassagem
    
    def getId(self):
        return self.idPassagem
            
    def setIdVoo(self, idVoo):
        self.idVoo = idVoo
    
    def getIdVoo(self):
        return self.idVoo

    def setDataDeCompra(self,dataDeCompra):
        self.dataDeCompra = dataDeCompra
    
    def getDataDeCompra(self):
        return self.dataDeCompra
            
    def setIdUsuario(self, idUsuario):
        self.idUsuario = idUsuario
    
    def getIdUsuario(self):
        return self.idUsuario

user = Usuario(idUsuario=1 ,nome="idUsuario um", cpf="12412312523", endereco="Rua 1", email="idUsuario1@ufu.br")
print(user.__repr__())

aeroporto1 = Aeroporto(idAeroporto="1", nome = "garulhos", pais="Brasil", cidade="Sao Paulo")
print(aeroporto1.__repr__())
aeroporto2 = Aeroporto(idAeroporto="2", nome = "base interespacial", pais="Brasil", cidade="Sao Jorge")
print(aeroporto2.__repr__())
aviao = Aviao(idAviao="1", qtAssentosEconomicos=3, qtAssentosExecutivos=5)
print(aviao.__repr__())

idVoo = Voo(idVoo=1, idAviao=aviao.getIdAviao(), dataDeSaida="12-03-2023", idAeroportoSaida=aeroporto1.getIdAeroporto(), dataDeChegada="21-03-2023", idAeroportoChegada=aeroporto2.getIdAeroporto())
print(idVoo.__repr__()) 

passagem = Passagem(idPassagem=1, idVoo=idVoo.getIdVoo(), dataDeCompra="28-01-2023", idUsuario=user.getIdUsuario())
print(passagem)