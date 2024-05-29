from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from datetime import datetime
from utils.logger.logger import request_logger, response_logger
from utils.logger.logger_schema import ResponseLoggerSchema, RequestLoggerSchema


class CustomLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith("/api/"):
            response = await call_next(request)
            response_body = [chunk async for chunk in response.body_iterator]
            response_body_str = b''.join(response_body).decode('utf-8')
            
            request_message: RequestLoggerSchema = {
                "date_time": str(datetime.now()),
                "host": request.client.host,
                "path": request.url.path,
                "method": request.method,
                "status": str(response.status_code),
            }
            
            response_message: ResponseLoggerSchema = {
                "date_time": str(datetime.now()),
                "host": request.client.host,
                "path": request.url.path,
                "method": request.method,
                "status": str(response.status_code),
                "response_data": response_body_str
            }
            
            request_logger.info(request_message)
            response_logger.info(response_message)

            # Возврат тела ответа
            new_response = Response(
                content=response_body_str,
                status_code=response.status_code,
                headers=dict(response.headers),
                media_type=response.media_type
            )
            return new_response
        else:
            return await call_next(request)