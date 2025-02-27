from fastapi import Request
from fastapi.responses import JSONResponse

from core.errors.exeptions import BaseAPIException


def handle_api_exceptions(request: Request, exc: BaseAPIException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )
