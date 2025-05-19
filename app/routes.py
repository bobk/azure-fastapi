from fastapi import APIRouter, Request, Path

from . import utility
from . import mylogger

router = APIRouter()

@router.get("/")
def root(request: Request):
    """
    d
    """
    mylogger.mylog("test of /")
    return {"message": "Hello World"}


@router.get("/resources/{res_type}", summary="foo")
def res_get(
    request: Request,
    res_type: str = Path(..., description="foo2")
    ):
    """
        ddd
    """

    mylogger.mylog(utility.config_json)

    call = 'vm_list'

    return utility.make_call(call)
