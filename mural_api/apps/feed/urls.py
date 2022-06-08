import fastapi_users
from fastapi import APIRouter, Depends, Request, HTTPException, status

from mural_api.apps.user.models import User
from mural_api.apps.feed.schema import InformativeCardCreate, InformativeCardRead
from mural_api.apps.feed.manager import InformativeCardManager, get_card_manager




def create_card_router(
    current_user
) -> APIRouter:
    
    router = APIRouter()

    @router.post(
        "/card",
        response_model=InformativeCardRead,
        name="card:create",
    )
    async def create_informative_card(
        request: Request,
        card_create: InformativeCardCreate,
        card_manager: InformativeCardManager = Depends(get_card_manager),
        user: User = Depends(current_user)
    ):
        try:
            created_card = await card_manager.create(card_create, current_user=user)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"um error aconteceu. Exception={e}"
            )
        
        return created_card

    return router