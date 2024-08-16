from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI

from models import Gender, Role, User

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("c80e23e8-0518-4cb5-88c4-251edd0e0e2d"), 
        first_name="Jitendra",
        middle_name="Kumar",
        last_name="Yadav",
        gender=Gender.male,
        roles=[Role.admin]
    ),
    User(
        id=uuid4(), 
        first_name="Joe",
        # middle_name="von",
        last_name="Doe",
        gender=Gender.male,
        roles=[Role.student, Role.user]
    )
]

@app.get("/")
async def root():
    return {"Hello": "Fastapi"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return