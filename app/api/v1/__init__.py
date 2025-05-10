from fastapi import APIRouter

api_router = APIRouter()

# 여기에 다른 라우터들을 포함시킬 수 있습니다
# from .endpoints import users, items
# api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(items.router, prefix="/items", tags=["items"]) 