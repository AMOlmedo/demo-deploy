# ORM (Object Relational Model) en py facilita la interaacion con bd
# Utilizando objetos y clases en lugar de consultas.

from sqlalchemy import Column, String, Integer

from database import Base
# esto permite heredar de esta clase la estructura de la db

class User(Base):
    __tablename__ = "users"
    id =Column(Integer, primary_key=True, index = True )
    name = Column(String(30), index = True, unique=True)
    password = Column(String(30), index =True)
