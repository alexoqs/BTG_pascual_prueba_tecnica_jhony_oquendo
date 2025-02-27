from fastapi import APIRouter, Depends, HTTPException
from fastapi.exceptions import ValidationException
from core.errors.exeptions import DatabaseException
from core.use_cases.create_client_use_case import CreateClientUseCase
from application.api.dependencies.client_dependency import (
    get_create_use_case,
)
from infrastructure.api.models.client import ClientResponse


router = APIRouter(tags=["client"])


@router.post("/", response_model=ClientResponse)
async def create_client(
    client: ClientResponse,
    use_case: CreateClientUseCase = Depends(get_create_use_case)
) -> ClientResponse:
    try:
        create_client = await use_case.create_client(client)
        return ClientResponse(
            id=create_client.id,
            personal_info=create_client.personal_info,
            contact_info=create_client.contact_info,
            balance=create_client.balance,
            suscriptions=create_client.suscriptions
        )
    except ValidationException as e:
        raise HTTPException(status_code=400, detail=str(e))
    except DatabaseException as e:
        raise HTTPException(status_code=500, detail=str(e))
