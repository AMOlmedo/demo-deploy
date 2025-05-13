from pydantic   import BaseModel

#no represnta una tabla !!    que ??
# es un esquema de  datos
class UserData(BaseModel):
    id:int
    nombre: str
    apellido: str
    direccion:str
    email: str

class UserId(UserData):
    id: int