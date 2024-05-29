import logging

# Создаем файл обработчики
file_handler_request = logging.FileHandler("requests.log")
file_handler_response = logging.FileHandler("responses.log")

# Настраиваем логгер для запросов
request_logger = logging.getLogger("request_logger")
request_logger.addHandler(file_handler_request)
request_logger.setLevel(logging.INFO)

# Настраиваем логгер для ответов
response_logger = logging.getLogger("response_logger")
response_logger.addHandler(file_handler_response)
response_logger.setLevel(logging.INFO)

