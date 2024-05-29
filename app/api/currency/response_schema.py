from pydantic import BaseModel
from typing import List
 

class Currency(BaseModel):
    Cur_ID: int
    Date: str
    Cur_Abbreviation: str
    Cur_Scale: int
    Cur_Name: str
    Cur_OfficialRate: float
    
    
class CurrencyListResponse(BaseModel):
    status: str
    message: str
    data: List[Currency]
    
    
class CurrencyResponse(BaseModel):
    status: str
    message:str
    trend: str
    data: Currency | None