from operator import ge
from typing import List
from fastapi import FastAPI
from fastapi.params import Depends
from starlette.responses import RedirectResponse
import models,schemas
from Conexion import SessionLocal,engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

@app.get('/usuarios/',response_model=List[schemas.User])
def show_users(db:Session=Depends(get_db)):
    usuarios = db.query(models.User).all()
    return usuarios

@app.post('/usuarios/',response_model=schemas.User)
def create_users(entrada:schemas.User,db:Session=Depends(get_db)):
    usuario = models.User(username = entrada.username,nombre=entrada.nombre,rol=entrada.rol,estado=entrada.estado)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

@app.put('/usuarios/{usuario_id}',response_model=schemas.User)
def update_users(usuario_id:int,entrada:schemas.UserUpdate,db:Session=Depends(get_db)):
    usuario = db.query(models.User).filter_by(id=usuario_id).first()
    usuario.nombre=entrada.nombre
    db.commit()
    db.refresh(usuario)
    return usuario

@app.delete('/usuarios/{usuario_id}',response_model=schemas.Respuesta)
def delete_users(usuario_id:int,db:Session=Depends(get_db)):
    usuario = db.query(models.User).filter_by(id=usuario_id).first()
    db.delete(usuario)
    db.commit()
    respuesta = schemas.Respuesta(mensaje="Eliminado exitosamente")
    return respuesta

@app.get('/marcaciones/',response_model=List[schemas.Marcation])
def show_marcaciones(db:Session=Depends(get_db)):
    marcaciones = db.query(models.Marcation).all()
    return marcaciones

@app.post('/marcaciones/',response_model=schemas.Marcation)
def create_marcaciones(entrada:schemas.Marcation,db:Session=Depends(get_db)):
    marcacion = models.Marcation(fullname = entrada.fullname,email=entrada.email,area=entrada.area,geolocation=entrada.geolocation,hora=entrada.hora,fecha=entrada.fecha)
    db.add(marcacion)
    db.commit()
    db.refresh(marcacion)
    return marcacion
    
@app.delete('/marcaciones/{marcacion_id}',response_model=schemas.Respuesta)
def delete_mercaciones(marcacion_id:int,db:Session=Depends(get_db)):
    marcacion = db.query(models.Marcation).filter_by(id=marcacion_id).first()
    db.delete(marcacion)
    db.commit()
    respuesta = schemas.Respuesta(mensaje="Eliminado exitosamente")
    return respuesta

@app.get('/areas/',response_model=List[schemas.Area])
def show_areas(db:Session=Depends(get_db)):
    areas = db.query(models.Area).all()
    return areas

@app.post('/areas/',response_model=schemas.Area)
def create_areas(entrada:schemas.Area,db:Session=Depends(get_db)):
    area = models.Area(area = entrada.area)
    db.add(area)
    db.commit()
    db.refresh(area)
    return area

@app.delete('/areas/{area_id}',response_model=schemas.Respuesta)
def delete_area(area_id:int,db:Session=Depends(get_db)):
    area = db.query(models.Area).filter_by(id=area_id).first()
    db.delete(area)
    db.commit()
    respuesta = schemas.Respuesta(mensaje="Eliminado exitosamente")
    return respuesta

@app.put('/areas/{area_id}',response_model=schemas.Area)
def update_areas(area_id:int,entrada:schemas.AreaUpdate,db:Session=Depends(get_db)):
    area = db.query(models.Area).filter_by(id=area_id).first()
    area.area=entrada.area
    db.commit()
    db.refresh(area)
    return area

@app.get('/geolocation/',response_model=List[schemas.Geolocation])
def show_geolocations(db:Session=Depends(get_db)):
    geolocations = db.query(models.Geolocation).all()
    return geolocations

@app.post('/geolocation/',response_model=schemas.Geolocation)
def create_geolocations(entrada:schemas.Geolocation,db:Session=Depends(get_db)):
    geolocation = models.Geolocation(area= entrada.area, geolocation = entrada.geolocation)
    db.add(geolocation)
    db.commit()
    db.refresh(geolocation)
    return geolocation

@app.delete('/geolocation/{geolocation_id}',response_model=schemas.Respuesta)
def delete_geolocation(geolocation_id:int,db:Session=Depends(get_db)):
    geolocation = db.query(models.Geolocation).filter_by(id=geolocation_id).first()
    db.delete(geolocation)
    db.commit()
    respuesta = schemas.Respuesta(mensaje="Eliminado exitosamente")
    return respuesta

@app.put('/geolocation/{geolocation_id}',response_model=schemas.Geolocation)
def update_geolocations(geolocation_id:int,entrada:schemas.GeolocationUpdate,db:Session=Depends(get_db)):
    geolocation = db.query(models.Geolocation).filter_by(id=geolocation_id).first()
    geolocation.area = entrada.area
    geolocation.geolocation = entrada.geolocation
    db.commit()
    db.refresh(geolocation)
    return geolocation