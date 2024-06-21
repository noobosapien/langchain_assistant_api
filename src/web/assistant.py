from fastapi import APIRouter
from service.chat import build_assistant
from model.request import Request
from model.response import Response

router = APIRouter(prefix="/assistant")

@router.post("/")
def create(req: Request) -> Response:
    input = req.input
    assistant = build_assistant()

    if not assistant:
        res = Response(role="assistant", content="Chat not implemented")
        return res
    else:
        content = assistant.run(input)
        res = Response(role="assistant", content=content)
        return res
