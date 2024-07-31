from pydantic import BaseModel

class Route(BaseModel):
    start:str
    finish:str