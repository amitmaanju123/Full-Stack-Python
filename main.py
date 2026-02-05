
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# 2️. User Model (Data Structure)

class UserInfo(BaseModel):
    name: str
    email: str
    age: int


# For PATCH (partial update):

class UpdateUserInfo(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None



# 3️. Temporary Database (In-Memory)

user_db = {}


# 4️. POST – Create User

@app.post("/user_info/{user_id}")
def create_user(user_id: int, user: UserInfo):
    user_db[user_id] = user
    return {
        "message": "User created successfully",
        "data": user
    }


# 5️. GET – Fetch User

@app.get("/user_info/{user_id}")
def get_user(user_id: int):
    return user_db.get(user_id, "User not found")



# 6️. PUT – Full Update User


@app.put("/user_info/{user_id}")
def update_user(user_id: int, user: UserInfo):
    user_db[user_id] = user
    return {
        "message": "User fully updated",
        "data": user
    }



# 7️. PATCH – Partial Update User

@app.patch("/user_info/{user_id}")
def partial_update_user(user_id: int, user: UpdateUserInfo):
    stored_user = user_db.get(user_id)

    if not stored_user:
        return "User not found"

    updated_data = stored_user.dict()
    for key, value in user.dict(exclude_unset=True).items():
        updated_data[key] = value

    user_db[user_id] = updated_data
    return {
        "message": "User partially updated",
        "data": updated_data
    }


# 8️. DELETE – Remove User


@app.delete("/user_info/{user_id}")
def delete_user(user_id: int):
    user_db.pop(user_id, None)
    return {"message": "User deleted successfully"}




# 🔁 How FastAPI Works (Flow)


''' Client (Browser / Postman)
        ↓
HTTP Method (GET / POST / PUT / PATCH / DELETE)
        ↓
FastAPI Route
        ↓
Pydantic Validation
        ↓
Business Logic
        ↓
JSON Response   '''



# 📊 Summary Table

'''| Method | URL          | Use            |
   | ------ | ------------ | -------------- |
   | POST   | /user_info/1 | Create user    |
   | GET    | /user_info/1 | Fetch user     |
   | PUT    | /user_info/1 | Full update    |
   | PATCH  | /user_info/1 | Partial update |
   | DELETE | /user_info/1 | Delete user    |


'''
