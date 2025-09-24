from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["signin", "signup"]
)


@router.get('/signin')
async def signin():
    return {"Page": "Signin Page"}

@router.get('signup')
async def signup():
    return {"Page": "Signup Page"}