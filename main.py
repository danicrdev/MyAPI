from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional
# from fastapi import HTTPException



class Users(BaseModel):
	id: Optional[int]= None
	nickname:str = Field(min_length=4, max_length=10)
	mail:str 
	password:str = Field(min_length=5, max_length=50)

	class Config:
		schema_extra = {
			"example": {
			"id" : 1,
			"nickname" : "Juanidev",
			"mail": "foo@gmail.com",
			"password" : "MyPassword1234"
			}
		}


app=FastAPI()

users=[{
	"id": 1,
	"nickname":"danicrdev",
	"mail": "hi@gmail.com",
	"password": "AAjsnwiwl"
},
{
	"id": 2,
	"nickname":"jueni",
	"mail": "jueni@gmail.com",
	"password": "123412bbsbf"
},
{
	"id": 3,
	"nickname":"aleco",
	"mail": "aleco@gmail.com",
	"password": "1234Jsjahisajsa"
}
]

@app.get("/")
def root():
	return {'Hello': 'World'}

#returns a JSON with users
@app.get("/users", tags=["users"])
def get_users():
	return JSONResponse(content=users)

#Find and returns a user by their id
@app.get("/users/{user_id}", tags=["users"])
def get_user(user_id:int):
	for item in users:
		if item["id"]==user_id:
			return JSONResponse(content=item)
	return JSONResponse(status_code=404, content=[])


#Create a new user
@app.post("/create_user", tags=["users"])
def create_new_user(user: Users):
	users.append(user.dict())
	return JSONResponse(content={'Message': 'usuario creado con exito'})

#Update an existent user
@app.put("/users/{user_id}", tags=["users"])
def update_user(id:int, user:Users):
	for item in users:
		if item["id"]==id:
			item["nickname"]=user.nickname
			item["mail"]=user.mail
			item["password"]=user.password
			return JSONResponse(content={"message": "usuario actualizado"})
	return JSONResponse(content="id de usuario no encontrado")		


#Delete an existent user
@app.delete("/users/{user_id}", tags=["users"])
def delete_user(id:int):
	for item in users:
		if item["id"]==id:
			users.remove(item)
			return JSONResponse(content="Usuario eliminado")



