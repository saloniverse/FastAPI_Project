from fastapi import APIRouter, Query, status
from typing import Optional, List
from schemas.server import ServerRead
from data.data import fake_db

router = APIRouter()
print("Current fake db:", fake_db,)

@router.get(
        "",
        response_model=List[ServerRead],
        status_code=status.HTTP_200_OK,
        name="get_servers"
)
async def get_servers(
        hostname: Optional[str] = Query(None),
        server_class: Optional[str] = Query(None)
        ) -> List[ServerRead]:
        return [
                server for server in fake_db
                if (hostname is None or server["hostname"] == hostname) and (server_class is None or server["server_class"] == server_class)
        ]