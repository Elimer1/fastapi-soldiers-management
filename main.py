from fastapi import FastAPI, status, HTTPException
from utils.io import json_to_list, list_to_json
from logger_config import logger

app = FastAPI()

@app.get("/soldiers")
def get_soldiers():
    return json_to_list()