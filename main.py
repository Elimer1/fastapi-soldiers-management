from fastapi import FastAPI, status, HTTPException
from utils.io import json_to_list, list_to_json
from logger_config import logger

app = FastAPI()

@app.get("/soldiers")
def get_soldiers():
    return json_to_list()


@app.get("/soldiers/{id}")
def get_soldier_by_id(id):
    soldier_list = json_to_list()
    for soldier in soldier_list:
        if soldier["id"] == id:
            return soldier
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")