from pydantic import BaseModel
from typing import List


class Currency(BaseModel):
    cur_id: int 
    cur_parent_id: int
    cur_code: int
    cur_abbreviation: str
    cur_name: str
    cur_name_bel: str
    cur_name_eng: str
    cur_quot_name: str
    cur_quot_name_bel: str 
    Cur_QuotName_Eng: str
    Cur_NameMulti: str
    Cur_Name_BelMulti: str
    Cur_Name_EngMulti: str
    Cur_Scale: str
    Cur_Periodicity: str
    Cur_DateStart: str
    Cur_DateEnd: str
    
    
class CurrencyListResponse(BaseModel):
    status: str
    message: str
    data: List[Currency]