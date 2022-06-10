from typing import List
from fastapi import APIRouter, Depends, Request, HTTPException, status

from mural_api.apps.user.models import User
from mural_api.apps.feed.schema import InformativeCardCreate, InformativeCardRead
from mural_api.apps.feed.manager import InformativeCardManager, get_card_manager




def create_card_router(current_user) -> APIRouter:
    router = APIRouter()

    @router.post("/card", response_model=InformativeCardRead, name="card:create")
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


def get_card_router() -> APIRouter:
    router = APIRouter()

    @router.get("/card/{card_id}", response_model=InformativeCardRead, name="card:get")
    async def get_informative_card(
        card_id: str,
        card_manager: InformativeCardManager = Depends(get_card_manager),
    ):
        card = await card_manager.get(card_id)
        return card

    return router

def fetch_card_router() -> APIRouter:
    router = APIRouter()

    @router.get("/card", response_model=list[InformativeCardRead], name="card:fetch")
    async def fetch_informative_cards(card_manager: InformativeCardManager = Depends(get_card_manager)):
        return await card_manager.fetch()

    return router