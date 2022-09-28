import json
from typing import List, Union
from fastapi import FastAPI
import os, random

app = FastAPI()

@app.get("/")
async def get_all_event_types():
    return json.dumps({"event_types": "msapersoncontactchange"})


@app.get("/fromDIM")
async def get_events():
    randomFile = random.choice(os.listdir("./data"))
    f = open(f"./data/{randomFile}")
    json_content = json.load(f)
    # Return random list of events by choosing a random file from the /data folder.
    return json_content


@app.post("/toDIM")
async def send_event(event: str):
    # TODO Return type must be learned from BIT engineers.
    return {"thank you. Message is received."}
