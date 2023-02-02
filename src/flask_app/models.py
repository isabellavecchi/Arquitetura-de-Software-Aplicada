import datetime

from sqlalchemy import Column, Integer, String, MetaData, UniqueConstraint, ForeignKey, Table, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

###################### Usuario ######################

class User(Base):   #Client é filho da classe Base
    __tablename__ = 'tb_usuario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(80)) #VARCHAR
    email = Column(String(100), unique=True)
    senha = Column(String(200))

    def __init__(self, usuario):
        if(usuario.getId() is not None):
            self.id = usuario.getId()
        self.nome = usuario.getNome()
        self.email = usuario.getEmail()
        self.senha = usuario.getSenha()

    def serialize(self):
        """Return a dictionary"""
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha
        }

    def __repr__(self):
        return 'ID: %s\nusuario: %s\nEmail: %s\nsenha: %s\n' % (self.id, self.nome, self.email, self.senha)


###################### Aeroporto ######################

class Airport(Base):
    """This class defines the tb_aeroporto table"""

    __tablename__ = 'tb_aeroporto'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(256), nullable=False)
    estado = Column(String(256), nullable=False)
    cidade = Column(String(256), nullable=False)
    # flights = relationship('Flight', backref='airport', lazy=True)

    def __init__(self, aeroporto):
        """Initialize the airport with the airport details"""
        if(aeroporto.getId() is not None):
            self.id = aeroporto.getId()
        self.nome = aeroporto.getNome()
        self.estado = aeroporto.getEstado()
        self.cidade = aeroporto.getCidade()

    def serialize(self):
        """Return a dictionary"""
        return {
            'id': self.id,
            'nome': self.nome,
            'estado': self.estado,
            'cidade': self.cidade
        }

    # @staticmethod
    # def get_all():
    #     return Airport.query.all()

    def __repr__(self):
        return 'tb_aeroporto: {}'.format(self.nome)


###################### Aviao ######################

class Airplane(Base):
    """This class defines the tb_aviao table"""

    __tablename__ = 'tb_aviao'

    id = Column(Integer, primary_key=True, autoincrement=True)
    qt_total_assentos = Column(Integer, nullable=False)

    def __init__(self, aviao):
        """Initialize the airplane details"""
        if(aviao.getId() is not None):
            self.id = aviao.getId()
        self.qt_total_assentos = aviao.getQtAssentosTotais()

    def serialize(self):
        """Return a dictionary"""
        return {
            'id': self.id,
            'qt_total_assentos': self.qt_total_assentos
        }

    def __repr__(self):
        return 'Airplane: {}'.format(self.reg_number)


###################### Voo ######################

class Flight(Base):
    """This class defines the flight schedules table"""

    __tablename__ = 'tb_voo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_aviao = Column(Integer, ForeignKey('tb_aviao.id'),
                            nullable=False)
    qt_lugares_disponiveis = Column(Integer, default=0)
    data_saida = Column(DateTime, nullable=False)
    id_aeroporto_saida = Column(Integer, ForeignKey('tb_aeroporto.id'),
                                     nullable=False)
    data_chegada = Column(DateTime, nullable=False)
    id_aeroporto_chegada = Column(Integer, ForeignKey('tb_aeroporto.id'),
                                     nullable=False)
    preco = Column(Float, default=0)

    def __init__(self, voo):
        """Initialize the flight details"""
        if(voo.getId() is not None):
            self.id = voo.getId()
        self.id_aviao = voo.getIdAviao()
        self.qt_lugares_disponiveis = voo.getQtLugaresDisponiveis()
        self.data_saida = voo.getDataDeSaida()
        self.id_aeroporto_saida = voo.getIdAeroportoSaida()
        self.data_chegada = voo.getDataDeChegada()
        self.id_aeroporto_chegada = voo.getIdAeroportoSaida()
        self.preco = voo.getPreco()

    # def get_arrival_airport(self):
    #     return Airport.query.filter_by(id=self.id_aeroporto_chegada).first()

    def serialize(self):
        """Return a dictionary"""
        self.arrival_airport = self.get_arrival_airport()
        return {
            'id': self.id,
            'id_aviao': self.id_aviao,
            'qt_lugares_disponiveis': self.qt_lugares_disponiveis,
            'data_saida': self.data_saida,
            'id_aeroporto_saida': self.id_aeroporto_saida,
            'data_chegada': self.data_chegada,
            'id_aeroporto_chegada': self.id_aeroporto_chegada,
            'preco': self.preco
        }

    # @staticmethod
    # def get_all():
    #     return Flight.query.all()

    def __repr__(self):
        return 'Flight: {}'.format(self.id)


###################### Passagem ######################
class Booking(Base):
    """This class defines the tb_passagem table"""

    __tablename__ = 'tb_passagem'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_voo = Column(Integer, ForeignKey('tb_voo.id'),
                            nullable=False)
    data_compra = Column(DateTime, default=datetime.datetime.now())
    nome_comprador = Column(String(256), nullable=False)
    cpf_comprador = Column(String(17), nullable=False)
    # email_status = Column(String(120), nullable=False, default='pending')

    def __init__(self, passagem):
        """Initialize the booking with the reservation details"""
        if(passagem.getId() is not None):
            self.id = passagem.getId()
        self.id_voo = passagem.getIdVoo()
        self.nome_comprador = passagem.getNomeComprador()
        self.cpf_comprador = passagem.geCPFcomprador()

    def serialize(self):
        """Return a dictionary"""
        return {
            "id": self.id,
            "id_voo": self.id_voo,
            "data_compra": self.data_compra,
            "nome_comprador": self.nome_comprador,
            "cpf_comprador": self.cpf_comprador
        }

    def __repr__(self):
        return 'tb_passagem: {}'.format(self.id)