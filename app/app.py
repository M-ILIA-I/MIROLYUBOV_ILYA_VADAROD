from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
import os


load_dotenv()

app = FastAPI(
    title="My Awesome API",
    description="This is a test project for VODOROD",
    version="1",
    contact={
        "name": "MIROLYUBOV ILYA",
        "url": "@ILIAMV - tg",
        "email": "ilyamir1@mail.ru",
    }
)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=os.getenv("HOST"),
        port=os.getenv("PORT")
    )