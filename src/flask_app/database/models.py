import datetime

from sqlalchemy import Column, Integer, String, MetaData, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from flask_app.usuario.Usuario import Usuario
from flask_app.aeroporto.Aeroporto import Aeroporto
from flask_app.aviao.Aviao import Aviao
from flask_app.passagem.Passagem import Passagem
from flask_app.voo.Voo import Voo

Base = declarative_base()

class User(Base):   #Client é filho da classe Base
    __tablename__ = 'tb_usuario'
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(80)) #VARCHAR 
    cpf = Column(String(11), unique=True)
    endereco = Column(String(200))
    email = Column(String(100), unique=True)

    def __init__(self, usuario):
        self.nome = usuario.getNome()
        self.cpf = usuario.getCPF()
        self.endereco = usuario.getEndereco()
        self.email = usuario.getEmail()

    # def __repr__(self):
    #     return 'usuario: %s\nEndereco: %s\nEmail: %s\n' % (self.nome, self.endereco, self.email)

"""user = Usuario(nome="Usuario um", endereco="Rua 1", email="Usuario1@ufu.br")

r1 = User(user)

print(r1)"""

class Airport(Base):
    """This class defines the airports table"""

    __tablename__ = 'tb_aeroporto'

    id_aeroporto = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(256), nullable=False)
    country = Column(String(256), nullable=False)
    city = Column(String(256), nullable=False)
    # flights = relationship('Flight', backref='airport', lazy=True)

    def __init__(self, nome, country, city):
        """Initialize the airport with the airport details"""
        self.nome = nome
        self.country = country
        self.city = city

    def serialize(self):
        """Return a dictionary"""
        return {
            'airport_id': self.id_aeroporto,
            'airport_nome': self.nome,
            'country': self.country,
            'city': self.city
        }

    # @staticmethod
    # def get_all():
    #     return Airport.query.all()

    def __repr__(self):
        return 'airports: {}'.format(self.nome)


class Airplane(Base):
    """This class defines the airplanes table"""

    __tablename__ = 'tb_aviao'

    id_aviao = Column(Integer, primary_key=True)
    # assentos_todos = Column(Integer, nullable=False)
    assentos_economicos = Column(Integer, nullable=False)
    assentos_executivos = Column(Integer, nullable=False)
    # flights = relationship('Flight', backref='airplane', lazy=True)

    def __init__(self, reg_number, assentos_economicos, assentos_executivos,
                 first_class_seats):
        """Initialize the airplane details"""
        self.reg_number = reg_number
        self.assentos_todos = assentos_economicos + assentos_executivos
        self.assentos_economicos = assentos_economicos
        self.assentos_executivos = assentos_executivos
        # self.first_class_seats = first_class_seats

    def serialize(self):
        """Return a dictionary"""
        return {
            'id_airplane': self.id,
            'reg_number': self.reg_number,
            'assentos_executivos': self.assentos_executivos,
            'assentos_economicos': self.assentos_economicos,
            'assentos_todos': self.assentos_todos
        }

    # @staticmethod
    # def get_all():
    #     return Airplane.query.all()

    def __repr__(self):
        return 'Airplane: {}'.format(self.reg_number)


class Flight(Base):
    """This class defines the flight schedules table"""

    __tablename__ = 'tb_voo'

    id_voo = Column(Integer, primary_key=True)
    departure_date = Column(DateTime, nullable=False)
    id_departure_airport = Column(Integer, ForeignKey('airports.id_aeroporto'),
                                     nullable=False)
    arrival_date = Column(DateTime, nullable=False)
    id_arrival_airport = Column(Integer, nullable=False)
    status = Column(String(256), default='upcoming')
    id_airplane = Column(Integer, ForeignKey('airplanes.id'),
                            nullable=False)
    booked_business = Column(Integer, default=0)
    booked_economy = Column(Integer, default=0)
    bookings = relationship('Booking', backref='flight', lazy=True)

    def __init__(self, departure_date, id_departure_airport, arrival_date,
                 id_arrival_airport, id_airplane):
        """Initialize the flight details"""
        self.departure_date = departure_date
        self.id_departure_airport = id_departure_airport
        self.arrival_date = arrival_date
        self.id_arrival_airport = id_arrival_airport
        self.id_airplane = id_airplane

    # def get_arrival_airport(self):
    #     return Airport.query.filter_by(id=self.id_arrival_airport).first()

    def serialize(self):
        """Return a dictionary"""
        self.arrival_airport = self.get_arrival_airport()
        return {
            'id_voo': self.id_voo,
            'departure_date': self.departure_date,
            'departure_airport': self.airport.nome,
            'departure_city': self.airport.city,
            'arrival_date': self.arrival_date,
            'arrival_airport': self.arrival_airport.nome,
            'arrival_city': self.arrival_airport.city,
            'flight_status': self.status
        }

    # @staticmethod
    # def get_all():
    #     return Flight.query.all()

    def __repr__(self):
        return 'Flight: {}'.format(self.id)

class Booking(Base):
    """This class defines the bookings table"""

    __tablename__ = 'bookings'

    id_passagem = Column(Integer, primary_key=True)
    data_compra = Column(DateTime, nullable=False)
    id_usuario = Column(Integer, ForeignKey('users.id_usuario'), nullable=False)
    id_voo = Column(Integer, ForeignKey('flights.id_voo'),
                          nullable=False)
    # email_status = Column(String(120), nullable=False, default='pending')

    def __init__(self, id_usuario, id_voo, status='pending'):
        """Initialize the booking with the reservation details"""
        self.data_compra = datetime.datetime.now()
        self.id_usuario = id_usuario
        self.id_voo = id_voo
        # self.email_status = status

    def serialize(self):
        """Return a dictionary"""
        return {
            "data_compra": self.data_compra,
            "booked_by": self.owner.nome,
            # "email_status": self.email_status
        }

    def __repr__(self):
        return 'bookings: {}'.format(self.id)