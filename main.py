import json
from typing import List, Union
from fastapi import FastAPI
import os, random
import globallogger

logger = globallogger.setup_custom_logger('app')

app = FastAPI()

@app.get("/")
async def get_all_event_types():
    """Use this service to learn about all existing/available event types.  """
    return json.load(open(f"./data/eventTypes/all.json"))

@app.get("/fromDIM")
async def get_events():
    """Use this service to fetch an array of events, which was "issued" by the BIT."""
    randomFile = random.choice(os.listdir("./data/fromDIM"))
    f = open(f"./data/fromDIM/{randomFile}")
    json_content = json.load(f)
    # Return random list of events by choosing a random file from the /data folder.
    return json_content


@app.post("/toDIM")
async def send_event(event: str):
    """Use this service to post a event to the BIT."""
    # TODO Return type must be learned from BIT engineers.
    logger.info(f"Event for /toDIM received: {event}")
    return {"your event": f"{event}"}
