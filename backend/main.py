#v1.2
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
from database import engine, localSession
from schemas import UserData, UserId
from models import Base

Base.metadata.create_all(bind=engine) 
#con esto se crean las tablas de la bd si no estan creadas/

app = FastAPI()  #creacion de la instacia FastAPI

def get_bd():
    db = localSession()
    try:
        yield db
    finally:
        db.close()
       
@app.get('/')   #un decorador ??  utilizado en la ruta base

def root(): 
    return 'Hola soy la API!! v1.3.0 '

#para ejecutar la app se utiliza en cl:
#  $uvicorn main:app --reload 

#rutas de conexion al a bd

@app.get('/api/users/', response_model=list[UserId])
def get_users(db: Session = Depends(get_bd)):
    return crud.get_users(db=db)

@app.get('/api/users/{id:int}',response_model=UserId)
def get_user(id, db: Session=Depends(get_bd)):
    user_by_id=crud.get_user_by_id(db=db, id=id)
    if user_by_id:
        return user_by_id
    raise HTTPException(status_code=404, detail='Usuario no encontrado!! papa')

@app.post('/api/users/', response_model=UserId)
def create_user(user: UserData, db:Session = Depends(get_bd)):
    check_name = crud.get_user_by_name(db=db, name =user.name)
    if check_name :
        raise HTTPException(status_code=400, detail='user already exist.')
    return crud.create_user(db=db, user=user)

