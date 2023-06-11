from fastapi import FastAPI

from event_service import addEvent, getAlert
from model import Event

app = FastAPI()


@app.post("/event")
def add_event(event:Event):
    addEvent(event)
    return {"message": "event is added"}

@app.get("/alert")
def get_alert(id:int):
    return getAlert(id)