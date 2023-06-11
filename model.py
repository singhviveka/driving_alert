from pydantic import BaseModel


class Event(BaseModel):
    timestamp: str
    is_driving_safe: bool