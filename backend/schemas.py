from pydantic   import BaseModel

#no represnta una tabla !!    que ??
# es un esquema de  datos
class UserData(BaseModel):
    name: str
    password: str

class UserId(UserData):
    id: int