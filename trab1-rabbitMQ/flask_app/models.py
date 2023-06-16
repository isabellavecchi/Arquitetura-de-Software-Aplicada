from sqlalchemy import Column, Integer, String, MetaData, UniqueConstraint
#from database import Base
from sqlalchemy.ext.declarative import declarative_base
from student import Estudante

Base = declarative_base()

class TbEstudante(Base):   #TbEstudante é filho da classe Base
    __tablename__ = 'tb_estudante'
    matricula = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(80)) #VARCHAR 
    cpf = Column(String(11), unique=True)
    endereco = Column(String(200))
    email = Column(String(100), unique=True)

    def __init__(self, estudante):
        self.nome = estudante.getNome()
        self.cpf = estudante.getCPF()
        self.endereco = estudante.getEndereco()
        self.email = estudante.getEmail()

    # def __repr__(self):
    #     return 'Estudante: %s\nMatricula: %s\nEndereco: %s\nEmail: %s\n' % (self.nome, self.matricula, self.endereco, self.email)
    
    def getMatricula(self):
        return self.matricula
    
    def getNome(self):
        return self.nome
    
    def getCPF(self):
        return self.cpf

    def getEndereco(self):
        return self.endereco

    def getEmail(self):
        return self.email
    
    

    def setNome(self,nome):
        self.nome = nome

    def setCPF(self,nome):
        self.nome = nome
            
    def setEndereco(self, endereco):
        self.endereco = endereco
            
    def setEmail(self,email):
        self.email = email

''' student1 = Estudante(nome="estudante um", endereco="Rua 1", email="estudante1@ufu.br")
student2 = Estudante(matricula="13", nome="estudante dois", endereco="Rua 2", email="estudante2@ufu.br")

r1 = TbEstudante(student1)
r2 = TbEstudante(student2)

print(r1)
print(r2) '''