import json
import re
import logging

class Aviao:
    #construtor
    def __init__(self, idAviao=None, qtTotalAssentos=None):
        try:
            self.idAviao = idAviao
            self.qtTotalAssentos = qtTotalAssentos
        except Exception as e:
            logging.info(f'{e}')
            print(e)
            self = None

        logging.info('DADOS DE Aviao DENTRO DOS PADROES!!')

    def __iter__(self): #cria dicionario
        yield from{
            "idAviao": self.idAviao,
            "qtTotalAssentos": self.qtTotalAssentos,
        }.items()
    
    #envia uma estrutura em formato de dicionário (dict interage com o método iter)
    def __str__(self):
        return json.dumps(dict(self), ensure_ascii = False)
    
    #usado no momento que dou o print
    def __repr__(self):
        return 'Aviao: %s\nQtAssentosTotais: %s\n' % (self.getId(), self.getQtAssentosTotais())
    
    def printa(self):
        print(self.__repr__())

    # def from_json(json_file):
    #     return Aviao(json.load(dict(json_file), ensure_ascii = False))

    def to_json(self):
        return self.__str__()


    #VALIDACOES
    # GETTERS AND SETTERS

    def setId(self,idAviao):
        self.idAviao = idAviao
    
    def getId(self):
        return self.idAviao

    def setQtTotalAssentos(self,qtTotalAssentos):
        self.qtTotalAssentos = qtTotalAssentos
    
    def getQtAssentosTotais(self):
        return self.qtTotalAssentos

''' aviao = Aviao(idAviao="1", qtTotalAssentos=3, qtAssentosExecutivos=5)
print(aviao.__repr__()) '''