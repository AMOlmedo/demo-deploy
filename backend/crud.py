# No es un CRUD como tal solo para el ejm.

from sqlalchemy.orm import Session

from   models import User

from schemas import UserData

# fucniones q interactuan con la base de datos
def get_users(db:Session):
    return db.query(User).all()

def get_user_by_id(db:Session, id:int):
    return db.query(User).filter(User.id ==id).first()

def  get_user_by_name(db: Session, name:str):
    return db.query(User).filter(User.name == name).first()

#creacion de un user nuevo. el password no es el procedimiento correcto
#es a los fines practicos.
def create_user(db:Session, user:UserData):
    fake_password = user.password + '#fake'
    new_user = User(name=user.name, password=fake_password)
    db.add(new_user)
    db.commit()
    db.flush(new_user)
    return new_user
