from fastapi import FastAPI, status, HTTPException
from utils.io import json_to_list, list_to_json
from logger_config import logger

app = FastAPI()

@app.get("/soldiers")
def get_soldiers():
    return json_to_list()


@app.get("/soldiers/{id}")
def get_soldier_by_id(id: int):
    soldier_list = json_to_list()
    for soldier in soldier_list:
        if soldier["id"] == id:
            return soldier
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")


@app.post("/soldiers")
def add_soldier(new_soldier: dict):
    soldier_list = json_to_list()
    soldier_list.append(new_soldier)
    list_to_json(soldier_list)
    return {"message": "user added successfully"}


@app.put("/soldiers/{id}")
def update_soldier(id: int, new_soldier: dict):
    soldier_list = json_to_list()
    for soldier in soldier_list:
        if soldier["id"] == id:
            soldier.update(new_soldier)
    list_to_json(soldier_list)
    return {"message": "user updated successfully"}


@app.delete("/soldiers/{id}")
def delete_soldier(id: int):
    soldier_list = json_to_list()
    updated_soldier_list = [soldier for soldier in soldier_list if soldier["id"] != id]
    if len(soldier_list) == len(updated_soldier_list):
        raise HTTPException(404, "user not found")
    list_to_json(updated_soldier_list)
    return {"message": "soldier removed successfully"}