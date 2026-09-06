from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List


    
conf = ConnectionConfig(
    MAIL_USERNAME = "rovex.universe1@gmail.com",
    MAIL_PASSWORD = "jfjq gikq uqyc jrbq",
    MAIL_FROM = "rovex.universe1@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME="Vigil AI",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)



async def send_email(emails: List[str]):
    html = """<p>Hi, Thanks for registration. Our team will contect you soon.l</p> """

    message = MessageSchema(
        subject="Registration Confirmation",
        recipients=emails,
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    print("mail has been sent successfuly")
    return {"message": "email has been sent"}