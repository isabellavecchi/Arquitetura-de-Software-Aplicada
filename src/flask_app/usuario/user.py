import json
import re
import logging

class Usuario:
    #construtor
    def __init__(self, nome=None, cpf=None, endereco=None, email=None):
        try:
            if not (Usuario.validaNome(nome)):
                raise Exception("ALGUM CARACTERE DE [NOME] EH INVALIDO!!!")
            nums_cpf = Usuario.getNumsFromCPF(cpf)
            if not (Usuario.validaCPF(nums_cpf)):
                raise Exception("ALGUM CARACTERE DE [CPF] EH INVALIDO!!!")
            if not (Usuario.validaEndereco(endereco)):
                raise Exception("ALGUM CARACTERE DE [ENDERECO] EH INVALIDO!!!")
            if not (Usuario.validaEmail(email)):
                raise Exception("ALGUM CARACTERE DE [EMAIL] EH INVALIDO!!!")
            self.nome = nome
            self.cpf = nums_cpf
            self.endereco = endereco
            self.email = email
        except Exception as e:
            logging.info(f'{e}')
            print(e)
            self = None

        logging.info('DADOS DE USUARIO DENTRO DOS PADROES!!')

    def __iter__(self): #cria dicionario
        yield from{
            "nome": self.nome,
            "cpf": self.cpf,
            "endereco": self.endereco,
            "email": self.email
        }.items()
    
    #envia uma estrutura em formato de dicionário (dict interage com o método iter)
    def __str__(self):
        return json.dumps(dict(self), ensure_ascii = False)
    
    #usado no momento que dou o print
    def __repr__(self):
        return 'Usuario: %s\nEndereco: %s\nEmail: %s\n' % (self.getNome(), self.getCPF(), self.getEndereco(), self.getEmail())
    
    def printa(self):
        print(self.__repr__())

    # def from_json(json_file):
    #     return Usuario(json.load(dict(json_file), ensure_ascii = False))

    def to_json(self):
        return self.__str__()


    #VALIDACOES

    def validaNome(nome):
        pattern = re.compile("^[A-Za-záéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ ]+$")
        return pattern.findall(nome)

    def getNumsFromCPF(cpf):
        if isinstance(cpf, int):
            return cpf
        temp = re.findall(r'\d+', cpf)
        if len(temp) <= 1:
            nums_cpf = str(temp[0])
        else:
            nums_cpf = ''.join(temp)
        return nums_cpf
    
    def validaCPF(cpf):
        pattern = re.compile("^[0-9]{11}$")
        return pattern.findall(cpf)
    
    def validaEndereco(endereco):
            pattern = re.compile("^[A-Za-záéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ0-9,. ;-]+$")
            return pattern.findall(endereco)
    
    def validaEmail(email):
            pattern = re.compile("^[A-Za-z0-9+_.-]+[@]{1}[A-Za-z0-9-]+[.]{1}[A-Za-z.]+$")
            return pattern.findall(email)

    # GETTERS AND SETTERS

    def setNome(self,nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome

    def setCPF(self,nome):
        self.nome = nome
    
    def getCPF(self):
        return self.cpf
            
    def setEndereco(self, endereco):
        self.endereco = endereco
    
    def getEndereco(self):
        return self.endereco
            
    def setEmail(self,email):
        self.email = email
    
    def getEmail(self):
        return self.email

''' user = Usuario(nome="Usuario um", endereco="Rua 1", email="usuario1@ufu.br")
print(user.__repr__()) '''