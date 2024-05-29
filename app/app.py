from fastapi import FastAPI
from dotenv import load_dotenv
from .api.currency import exchange_rate_router
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
    }
)

app.include_router(exchange_rate_router)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=os.getenv("HOST"),
        port=os.getenv("PORT")
    )