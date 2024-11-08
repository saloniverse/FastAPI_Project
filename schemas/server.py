from pydantic import BaseModel

class ServerRead(BaseModel):
    hostname: str
    class_: str