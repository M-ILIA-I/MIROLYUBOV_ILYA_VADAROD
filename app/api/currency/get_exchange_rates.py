from fastapi import APIRouter, Path, Depends, Response
from .response_schema import CurrencyResponse
from ..handlers.currency.currency_handler import CurrencyHandler


router = APIRouter()

@router.get("/exchange_rates/", responses={200:{"model": CurrencyResponse}}, )
async def get_exchange_rates_by_date(
    date: str,
    currency_code: str,
    response: Response,
    handler: CurrencyHandler = Depends(CurrencyHandler),
):
    """information about the exchange rate for the specified day"""
    return await handler.get_exchange_rate(date=date, currency_code=currency_code, response=response)