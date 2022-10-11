import json
import glob
from typing import List, Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
)
import os, random
import globallogger

logger = globallogger.setup_custom_logger('app')

app = FastAPI(docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
        swagger_favicon_url="/static/favicon.ico",
    )

@app.get("/")
async def get_all_event_types():
    """Use this service to learn about all existing/available event types.  """
    return json.load(open(f"./data/eventTypes/all.json"))

@app.get("/fromDIM/{event_type}")
async def get_event(event_type:str):
    """Use this service to fetch an array of events, which was "issued" by the BIT."""
    #randomFile = random.choice(os.listdir("./data/fromDIM"))
    randomFile = random.choice(glob.glob(f"./data/fromDIM/{event_type}*"))
    f = open(f"{randomFile}")
    json_content = json.load(f)
    # Return random list of events by choosing a random file from the /data folder.
    return json_content


@app.post("/toDIM")
async def send_event(event: str):
    """Use this service to post a event to the BIT."""
    # TODO Return type must be learned from BIT engineers.
    logger.info(f"Event for /toDIM received: {event}")
    return {"your event": f"{event}"}
