from fastapi import FastAPI
from starlette.middleware.base import RequestResponseEndpoint
from dotenv import load_dotenv
from .api.currency import exchange_rate_router
from utils.middleware.logger_middleware import CustomLoggerMiddleware
import uvicorn
import os


load_dotenv()

app = FastAPI(
    title="My Awesome API",
    description="This is a test project for VODOROD",
    version="1",
    contact={
        "name": "MIROLYUBOV ILYA",
        "url": "https://github.com/M-ILIA-I/MIROLYUBOV_ILYA_VODOROD",
        "email": "ilyamir1@mail.ru",
    },
)

app.include_router(exchange_rate_router)

app.add_middleware(CustomLoggerMiddleware)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=os.getenv("HOST"),
        port=os.getenv("PORT")
    )