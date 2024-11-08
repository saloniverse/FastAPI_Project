from fastapi import APIRouter  
  
from api.routes.server import router as server_router  

router = APIRouter()  
  
  
router.include_router(server_router, prefix="/server")