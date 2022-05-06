from fastapi import APIRouter 
from models.user import User
from config.db import connect
from bson import ObjectId
from schemas.user import userEntity, usersEntity
user = APIRouter()

@user.get('/')
async def find_all_users():
    
    return usersEntity(connect["tptestunit"]["users"].find())


@user.post('/')
async def create_user(user: User):
    connect["tptestunit"]["users"].insert_one(dict(user))
    x = connect["tptestunit"]["users"].find()
    return userEntity(x[0])

@user.put('/{id}')
async def update_user(id, user: User):
    connect["tptestunit"]["users"].find_one_and_update({"_id": ObjectId(id)},{
        "$set": dict(user)
    })
    return userEntity(connect["tptestunit"]["users"].find_one({"_id": ObjectId(id)}))

@user.delete('/{id}')
async def update_user(id, user: User):
    return userEntity(connect["tptestunit"]["users"].find_one_and_delete({"_id": ObjectId(id)}))
