from fastapi import FastAPI
from application.api.routers import client
from application.api.handlers.error_handler import handle_api_exceptions
from core.errors.exeptions import BaseAPIException


app = FastAPI(
    title="Founds service API",
    description="API to manage founds",
    version="0.1.0",
    openapi_url="/api/v1/openapi.json",
)

app.include_router(client.router, prefix='/api/client', tags=['Client'])

app.add_exception_handler(BaseAPIException, handle_api_exceptions)


@app.get("/api/health")
def health_check():
    return {"status": "ok"}
