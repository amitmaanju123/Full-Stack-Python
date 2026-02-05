'''from fastapi import FastAPI


import requests

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Amit"}



@app.post("/hello")
def say_hello(name: str = "Guest"):
    return {"message": f"Hello, {name}!"}'''

# --------------------------------------------------------------------------------------------------------

'''# 1.GET Method (Read Data)

@app.get("/users")
def get_users():
    return {"users": ["Amit", "Rahul", "Neha"]}


# 2.POST Method (Create Data)


import pandas as pd

df = pd.DataFrame({
    "id": 101,
    "name": "amit",
    "age": 23,
    "skill": ["SQL","Python"]
})


@app.post("/user_info")
def user_info():
    return{
    "id": 101,
    "name": "amit",
    "age": 23,
    "skill": ["SQL","Python"]
}



# 3.PUT Method (Full Update)


@app.put("/users/{user_id}")
def update_user(user_id: int, user: user):
    return {
        "user_id": user_id,
        "updated_data": user
    }'''

# ----------------------------------------------------------------------------------------------------

# >cd OneDrive

# (base) C:\Users\DELL\OneDrive>cd Desktop

# (base) C:\Users\DELL\OneDrive\Desktop>cd fastapi_app

'''import pandas as pd

df = pd.DataFrame({
    "id": 101,
    "name": "amit",
    "age": 23,
    "skill": ["SQL","Python"]
})

# app=FastAPI()

@app.get("/user_info")
def user_info():
    return{
    "id": 101,
    "name": "amit",
    "age": 23,
    "skill": ["SQL","Python"]
}


# url = "https://github.com/renujindal89/API_5"

# data ={
#     "title": "Learn API",
#     "Body": "API are awesome",
#     "user-id": 1 
# }

# response = requests.post(url,json= data)
# print(response.status_code)
# print(response.json())




import pandas as pd

df = pd.DataFrame({
    "id": 101,
    "name": "amit",
    "age": 23,
    "skill": ["SQL","Python"]
})

# app=FastAPI()

@app.post("/user_info")
def user_info():
    return{
    "id": 101,
    "name": "amit",
    "age": 23,
    "skill": ["SQL","Python"]
}'''

# --------------------------------------------------------------------------------------------------------------------------------




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


# @app.patch("/tasks/{task_id}", status_code=status.HTTP_200_OK)
# def update_task_status(task_id: int, is_complete: str):
#     if task_id in task_dict:
#         task_dict[task_id].status = is_complete
#         return {"message": "Task updated", "task": task_dict[task_id].model_dump()}
#     else:
#         return {"error": "No Such Task"}
 



# from fastapi import HTTPException

# if not stored_user:
#     raise HTTPException(status_code=404, detail="User not found")



'''@app.patch("/user_info/{user_id}")
def partial_update_user(user_id: int, user: UpdateUserInfo):

    stored_user = user_db.get(user_id)

    if not stored_user:
        raise HTTPException(status_code=404, detail="User not found")

    updated_data = stored_user.copy()

    for key, value in user.dict(exclude_unset=True).items():
        updated_data[key] = value

    user_db[user_id] = updated_data

    return {
        "message": "User partially updated",
        "data": updated_data
    }'''





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