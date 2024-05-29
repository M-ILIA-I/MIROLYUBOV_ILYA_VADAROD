from fastapi import HTTPException
from dotenv import load_dotenv
from utils.get_crc32 import get_crc32
import requests
import datetime
import os 


load_dotenv()


class CurrencyHandler:
    async def get_exchange_rates_by_date(date:str):
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            url = f"{os.getenv("NBRB_API_URL")}?ondate={date_obj.strftime('%Y-%m-%d')}&periodicity=0"
            api_response = requests.get(url)
            
            if api_response.status_code != 200:
                raise HTTPException(status_code=api_response.status_code, detail="Failed to fetch data from NBRB API")

            data = api_response.json()
            print(data)
            
            crc32_value = get_crc32(api_response.text)
            print(crc32_value)
            
            # response.headers["X-CRC32"] = crc32_value
            return data

        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal Server Error")