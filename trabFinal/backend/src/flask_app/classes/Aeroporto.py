import json
import logging

class Aeroporto:
    #construtor
    def __init__(self, idAeroporto=None, nome=None, estado=None, cidade=None):
        try:
            self.idAeroporto = idAeroporto
            self.nome = nome
            self.estado = estado
            self.cidade = cidade
        except Exception as e:
            logging.info(f'{e}')
            print(e)
            self = None

        logging.info('DADOS DE Aeroporto DENTRO DOS PADROES!!')

    def __iter__(self): #cria dicionario
        yield from{
            "id": self.idAeroporto if hasattr(self,'idAeroporto') else None,
            "nomeAeroporto": self.nome,
            "cidade": self.cidade,
            "estado": self.estado
        }.items()
    
    #envia uma estrutura em formato de dicionário (dict interage com o método iter)
    def __str__(self):
        return json.dumps(dict(self), ensure_ascii = False)
    
    #usado no momento que dou o print
    def __repr__(self):
        return 'Aeroporto: %s\nNome: %s\nPaís: %s\ncidade: %s\n' % (self.getId(), self.getNome(), self.getEstado(), self.getCidade())
    
    def printa(self):
        print(self.__repr__())

    def from_json(json_file):
        print("aqui no from o filho do jota")
        print(json_file)
        if "id" in json_file:
            return Aeroporto(idAeroporto=json_file["id"], nome=json_file["nomeAeroporto"], estado=json_file["estado"], cidade=json_file["cidade"])
        else:
            return Aeroporto(nome=json_file["nomeAeroporto"], estado=json_file["estado"], cidade=json_file["cidade"])

    def to_json(self):
        return self.__str__()


    #VALIDACOES
    # GETTERS AND SETTERS

    def setId(self,idAeroporto):
        self.idAeroporto = idAeroporto
    
    def getId(self):
        return self.idAeroporto

    def setNome(self,idAeroporto):
        self.idAeroporto = idAeroporto
    
    def getNome(self):
        return self.nome
            
    def setEstado(self, estado):
        self.estado = estado
    
    def getEstado(self):
        return self.estado
            
    def setCidade(self,cidade):
        self.cidade = cidade
    
    def getCidade(self):
        return self.cidade

''' aeroporto = Aeroporto(idAeroporto="1", nome = "garulhos", estado="Brasil", cidade="Sao Paulo")
print(aeroporto.__repr__()) '''