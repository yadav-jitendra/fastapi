from typing import List
from uuid import uuid4
from fastapi import FastAPI

from models import Gender, Role, User

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(), 
        first_name="Jitendra",
        middle_name="Kumar",
        last_name="Yadav",
        gender=Gender.male,
        roles=[Role.admin]
    ),
    User(
        id=uuid4(), 
        first_name="Joe",
        middle_name="von",
        last_name="Doe",
        gender=Gender.male,
        roles=[Role.student]
    )
]

@app.get("/")
async def root():
    return {"Hello": "Fastapi"}

@app.get("/api/v1/users")
async def ftech_users():
    return db