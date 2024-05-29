from fastapi import HTTPException, Response, Depends
from dotenv import load_dotenv
from utils.get_crc32 import get_crc32
from app.api.currency.response_schema import CurrencyListResponse, CurrencyResponse
from sqlalchemy.ext.asyncio import AsyncSession
from database.db_connection import get_async_session
import requests
import datetime
import os 
import re


load_dotenv()


class CurrencyHandler:
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session
        self.api_url = os.getenv("NBRB_API_URL")

    
    def validate_date_format(self, date: str):
        """Проверка формата даты 'YYYY-MM-DD'"""
        # Регулярное выражение для проверки формата даты
        pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
        if not pattern.match(date):
            raise HTTPException(status_code=422, detail="Invalid date format. Date must be in YYYY-MM-DD format.")

    
    async def get_exchange_rates_by_date(self, date:str, response: Response):
        try:
            self.validate_date_format(date=date)
            
            date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
            
            url = f"{self.api_url}?ondate={date_obj.strftime('%Y-%m-%d')}&periodicity=0"
            api_response = requests.get(url)
            
            if api_response.status_code != 200:
                raise HTTPException(status_code=api_response.status_code, detail="Failed to fetch data from NBRB API")

            data = api_response.json()
            crc32_value = get_crc32(api_response.text)
            
            response.headers["X-CRC32"] = crc32_value
            return CurrencyListResponse(status="ok", message="The currency was successfully received", data=data)

        except HTTPException as e:
            return e
        
        
    async def get_exchange_rate(self, date: str, currency_code: str, response: Response):
        """Получить курс валюты на указанную дату"""
        try:
            self.validate_date_format(date=date)
            
            date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
            
            if date_obj.date() > datetime.datetime.now().date():
                raise HTTPException(status_code=400, detail="Incorrect date")
            
            url = f"{self.api_url}/{currency_code}?ondate={date_obj.strftime('%Y-%m-%d')}&periodicity=0"
            api_response = requests.get(url)
            
            if api_response.status_code != 200:
                raise HTTPException(status_code=api_response.status_code, detail="Failed to fetch data from NBRB API. This currency id probably does not exist.")
            
            data = api_response.json()
            previous_date_obj = date_obj - datetime.timedelta(days=1)
            previous_url = f"{self.api_url}/{currency_code}?ondate={previous_date_obj.strftime('%Y-%m-%d')}&periodicity=0"
            previous_response = requests.get(previous_url)
            
            if previous_response.status_code == 200:
                previous_data = previous_response.json()
                previous_rate = previous_data.get("Cur_OfficialRate", None)
                current_rate = data.get("Cur_OfficialRate", None)
                if previous_rate and current_rate:
                    if current_rate > previous_rate:
                        trend = "increased"
                    elif current_rate < previous_rate:
                        trend = "decreased"
                    else:
                        trend = "unchanged"
                    
                else:
                    trend = "unknown"
            else:
                trend = "unknown"

            crc32_value = get_crc32(api_response.text)
            response.headers["X-CRC32"] = crc32_value
            return CurrencyResponse(status="ok", message="The currency was successfully received", trend=trend, data=data)

        except HTTPException as e:
            return e