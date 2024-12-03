from fastapi import APIRouter

from app.models.example import ExampleIn, ExampleOut

router = APIRouter()


@router.post("/", description="Example Description", response_model=ExampleOut, status_code=200)
def read_root(example: ExampleIn):
    return example
