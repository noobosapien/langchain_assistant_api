from pydantic import BaseModel

class Request(BaseModel):
    input: str