from sqlalchemy import Column, Integer, String
from Conexion import Base

class User(Base):
    __tablename__ = 'usuario'
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(20))
    nombre = Column(String(200))
    rol = Column(String(20))
    estado = Column(Integer)
    
class Marcation(Base):
    __tablename__= 'marcation'
    id = Column(Integer,primary_key=True,index=True)
    fullname = Column(String(200))
    email = Column(String(50))
    area = Column(String(50))
    geolocation = Column(String(200))#-1655462.65400,12321.123123
    hora = Column(String(50))
    fecha = Column(String(50))
    
class Area(Base):
    __tablename__ = 'area'
    id = Column(Integer,primary_key=True,index=True)
    area = Column(String(50))
    
class Geolocation(Base):
    __tablename__ = 'geolocation'
    id = Column(Integer,primary_key=True,index=True)
    area = Column(String(50))
    geolocation = Column(String(200))#-1655462.65400,12321.123123
#MODELO DE LA BASE DE DATOS GENERAL
