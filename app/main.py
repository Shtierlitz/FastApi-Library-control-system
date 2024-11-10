from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from api.v1.endpoints import book, author, user
from core.exceptions import APIException
from pytz import timezone

app = FastAPI()
app.include_router(book.router, prefix="/api/v1/books", tags=["Books"])
app.include_router(author.router, prefix="/api/v1/authors", tags=["Authors"])
app.include_router(user.router, prefix="/api/v1/users", tags=["Users"])


@app.exception_handler(APIException)
async def api_exception_handler(request: Request, exc: APIException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

app.state.timezone = timezone("Europe/Kiev")

@app.middleware("http")
async def timezone_middleware(request, call_next):
    response = await call_next(request)
    # Здесь вы можете добавить обработку времени с учетом таймзоны, если необходимо
    return response