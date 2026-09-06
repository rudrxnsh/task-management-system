from fastapi import APIRouter, Depends, status, Request, BackgroundTasks
from sqlalchemy.orm import Session
from src.user import controller
from src.user.dtos import UserSchema, UserResponseSchema, LoginSchema
from src.utils.db import get_db

user_routes = APIRouter(prefix="/user")


@user_routes.post("/registration", response_model= UserResponseSchema ,status_code=status.HTTP_201_CREATED)
async def registration(body: UserSchema, bg_task: BackgroundTasks ,db: Session = Depends(get_db)):
    return await controller.registration(body, bg_task ,db)


@user_routes.post("/login", status_code=status.HTTP_202_ACCEPTED)
def login(body: LoginSchema, db: Session = Depends(get_db)):
    return controller.login(body, db)



@user_routes.get("/is_auth", status_code= status.HTTP_200_OK, response_model=UserResponseSchema)
def is_auth(request: Request, db: Session = Depends(get_db)):
    return controller.is_authenticated(request, db)
    