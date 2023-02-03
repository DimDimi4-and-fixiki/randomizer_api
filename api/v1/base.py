from fastapi import APIRouter

api_v1 = APIRouter(
    prefix='/api/v1',
    tags=['api_v1'],
    dependencies=[],
)


@api_v1.get('/ping')
async def ping() -> str:
    return 'pong from api_v1'
