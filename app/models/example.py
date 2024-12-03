from pydantic import BaseModel


class ExampleIn(BaseModel):
    name: str
    age: int


class ExampleOut(BaseModel):
    name: str
    age: int
