from typing import Optional
from pydantic import BaseModel
#MODELO DE LOS SERVICIOS
class User(BaseModel): #POST DETELE GET
    id:Optional[int]
    username:str
    nombre:str
    rol:str
    estado:int

    class Config:
        orm_mode =True

class UserUpdate(BaseModel): #PUT
    nombre:str
   
    class Config:
        orm_mode =True
        
class Marcation(BaseModel): #POST DETELE GET
    id:Optional[int]
    fullname:str
    email:str
    area:str
    geolocation:str
    hora: str
    fecha:str
    
    class Config:
        orm_mode =True
    
class Area(BaseModel): #POST DETELE GET
    id:Optional[int]
    area:str
    
    class Config:
        orm_mode =True

class AreaUpdate(BaseModel): #PUT
    area:str
    
    class Config:
        orm_mode =True
        
class Geolocation(BaseModel): #POST DETELE GET
    id:Optional[int]
    area:str
    geolocation:str
    
    class Config:
        orm_mode =True
        
class GeolocationUpdate(BaseModel): #PUT
    geolocation:str
    
    class Config:
        orm_mode =True
    
class Respuesta(BaseModel):#RESULTADO DE LAS OPERACIONES 
    mensaje:str