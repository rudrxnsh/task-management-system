from fastapi import HTTPException, status, Request, BackgroundTasks
from src.user.dtos import UserSchema, LoginSchema
from sqlalchemy.orm import Session
from src.user.models import UserModel
from pwdlib import PasswordHash
import jwt
from jwt.exceptions import InvalidTokenError
from src.utils.settings import settings
from datetime import datetime, timedelta
from src.utils.mail import send_email



password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

async def registration(body:UserSchema,bg_task: BackgroundTasks ,db: Session):
    
    ## 1. Username Validation
    is_user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if is_user:
        raise HTTPException(400, detail="This username already exist..")
    
    ## 2. Email Validation
    is_email = db.query(UserModel).filter(UserModel.email == body.email).first()
    if is_email:
        raise HTTPException(400, detail="This email is already exist...")
    
    hash_password = get_password_hash(body.password)
    
    new_user = UserModel(
        name = body.name,
        username = body.username,
        hashed_password = hash_password,
        email = body.email
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    ## Send Email Confirmation
    
    bg_task.add_task(send_email, [new_user.email])
    
    return new_user

def login(body: LoginSchema, db: Session):
    user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="YOu entered wrong username")
    
    if not verify_password(body.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = "you entered worng password")
    
    exp_time = datetime.now() + timedelta(minutes=settings.EXP_TIME)
    print(exp_time)
    token = jwt.encode({"_id": user.id, "exp": exp_time.timestamp()}, settings.SECRET_KEY, settings.ALGORITHM)
    
    
    return {"token": token}
    
    
## Token Sent 
def is_authenticated(request: Request, db: Session):
    
    try:
        
        token = request.headers.get("authorization")
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You're unauthorized")
        token = token.split(" ")[-1]

        data = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        
        user_id = data.get("_id")
        
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user: 
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You're Unauthorized")
    
    
        return user
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Session Time Expired")