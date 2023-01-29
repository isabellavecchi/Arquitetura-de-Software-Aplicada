import json
import re
import logging

class Aeroporto:
    #construtor
    def __init__(self, idAeroporto=None, nome=None, pais=None, cidade=None):
        try:
            self.idAeroporto = idAeroporto
            self.nome = nome
            self.pais = pais
            self.cidade = cidade
        except Exception as e:
            logging.info(f'{e}')
            print(e)
            self = None

        logging.info('DADOS DE Aeroporto DENTRO DOS PADROES!!')

    def __iter__(self): #cria dicionario
        yield from{
            "idAeroporto": self.idAeroporto,
            "nome": self.nome,
            "pais": self.pais,
            "cidade": self.cidade
        }.items()
    
    #envia uma estrutura em formato de dicionário (dict interage com o método iter)
    def __str__(self):
        return json.dumps(dict(self), ensure_ascii = False)
    
    #usado no momento que dou o print
    def __repr__(self):
        return 'Aeroporto: %s\nNome: %s\nPaís: %s\ncidade: %s\n' % (self.getIdAeroporto(), self.getNome(), self.getPais(), self.getCidade())
    
    def printa(self):
        print(self.__repr__())

    # def from_json(json_file):
    #     return Aeroporto(json.load(dict(json_file), ensure_ascii = False))

    def to_json(self):
        return self.__str__()


    #VALIDACOES
    # GETTERS AND SETTERS

    def setIdAeroporto(self,idAeroporto):
        self.idAeroporto = idAeroporto
    
    def getIdAeroporto(self):
        return self.idAeroporto

    def setNome(self,idAeroporto):
        self.idAeroporto = idAeroporto
    
    def getNome(self):
        return self.nome
            
    def setPais(self, pais):
        self.pais = pais
    
    def getPais(self):
        return self.pais
            
    def setCidade(self,cidade):
        self.cidade = cidade
    
    def getCidade(self):
        return self.cidade

''' aeroporto = Aeroporto(idAeroporto="1", nome = "garulhos", pais="Brasil", cidade="Sao Paulo")
print(aeroporto.__repr__()) '''