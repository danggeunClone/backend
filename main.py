from app.main import app
from app.api.v1 import api_router

app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    from app.core.config import settings
    
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    ) 