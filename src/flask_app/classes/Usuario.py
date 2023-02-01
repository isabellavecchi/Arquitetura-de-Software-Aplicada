import json
import re
import logging

class Usuario:
    #construtor
    def __init__(self, idUsuario=None, nome=None, email=None, senha=None):
        try:
            self.idUsuario = idUsuario
            self.nome = nome
            self.email = email
            novaSenha = Usuario.criptografarSenha(senha)
            self.senha = novaSenha
        except Exception as e:
            logging.info(f'{e}')
            print(e)
            self = None

        logging.info('DADOS DE USUARIO DENTRO DOS PADROES!!')

    def __iter__(self): #cria dicionario
        yield from{
            "id": self.id if hasattr(self,'idUsuario') else None,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha
        }.items()
    
    #envia uma estrutura em formato de dicionário (dict interage com o método iter)
    def __str__(self):
        return json.dumps(dict(self), ensure_ascii = False)
    
    #usado no momento que dou o print
    def __repr__(self):
        return 'Usuario: %s\nNome: %s\nEmail: %s\n' % (self.getId(), self.getNome(), self.getEmail())
    
    def printa(self):
        print(self.__repr__())

    def from_json(json_file):
        if "id" in json_file:
            return Usuario(idUsuario=json_file["id"], nome=json_file["nome"], email=json_file["email"], senha=json_file["senha"])
        else:
            return Usuario(nome=json_file["nome"], email=json_file["email"], senha=json_file["senha"])

    def to_json(self):
        return self.__str__()


    #VALIDACOES

    def criptografarSenha(senha):
        novaSenha = senha
        # não sei o que fazer ainda
        return novaSenha

    # GETTERS AND SETTERS

    def setId(self,idUsuario):
        self.idUsuario = idUsuario
    
    def getId(self):
        return self.idUsuario

    def setNome(self,nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
            
    def setEmail(self,email):
        self.email = email
    
    def getEmail(self):
        return self.email

    def setSenha(self,senha):
        self.senha = Usuario.criptografarSenha(senha)
    
    def getSenha(self):
        return self.senha

''' user = Usuario(nome="Usuario um", senha="12412312523", endereco="Rua 1", email="usuario1@ufu.br")
print(user.__repr__()) '''