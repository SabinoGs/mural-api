from fastapi import APIRouter, Request, HTTPException, status

from mural_api.apps.feed.schema import InformativeCardCreate, InformativeCardRead
from mural_api.apps.feed.erros import ErrorCode
router = APIRouter()


@router.post(
    "/card",
    response_model=InformativeCardRead,
    name="card:create",
)
async def create_informative_card(
    request: Request,
    card_create: InformativeCardCreate,
    card_manager: InformativeCardManager
):
    try:
        created_card = await card_manager.create(card_create, request=request)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="um error aconteceu."
        )
    
    return created_card