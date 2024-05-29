import logging


request_logger = logging.getLogger()

file_handler_request = logging.FileHandler("requests.log")

request_logger.handlers=[file_handler_request]

request_logger.setLevel(logging.INFO)

response_logger = logging.getLogger()

file_handler_response = logging.FileHandler("response.log")

response_logger.handlers=[file_handler_request]

response_logger.setLevel(logging.INFO)