from pydantic import BaseModel


class RequestLoggerSchema(BaseModel):
    date_time: str
    path: str
    method: str
    host: str | None
    status: str


class ResponseLoggerSchema(BaseModel):
    date_time: str
    path: str
    method: str
    host: str | None
    status: str
    response_data: str
