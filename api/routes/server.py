from fastapi import APIRouter, status

from schemas.server import ServerRead

from DB.data import fake_db

router = APIRouter()


@router.get(
        "",
        response_model=list[ServerRead],
        status_code=status.HTTP_200_OK,
        name="get_servers"
)
async def get_servers() -> list[ServerRead]:
    return [ServerRead(**server)for server in fake_db]