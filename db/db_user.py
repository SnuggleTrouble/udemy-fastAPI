from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from fastapi import HTTPException, status


# Once you have the model, create the db_user.
# This will provide the create user functionality to add data to our database.
def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
    )
    # add new data
    db.add(new_user)
    # save the data
    db.commit()
    # refresh to see it in the database
    db.refresh(new_user)
    # display changes
    return new_user


def get_all_users(db: Session):
    return db.query(DbUser).all()


def get_user(db: Session, id: int):
    # Queries the database and filters based on the provided condition.
    # You can filter more by adding .filter(DbUser.email == email)
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
        )
    return


def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with username {username} not found",
        )
    return user


def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
        )
    user.update(
        {
            DbUser.username: request.username,
            DbUser.email: request.email,
            DbUser.password: Hash.bcrypt(request.password),
        }
    )
    db.commit()
    return "OK. User successfully UPDATED"


def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
        )
    db.delete(user)
    db.commit()
    return "OK. User successfully DELETED"
