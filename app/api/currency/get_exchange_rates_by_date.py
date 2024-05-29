from fastapi import APIRouter, Path, Depends, Response
from .response_schema import CurrencyListResponse
from ..handlers.currency.currency_handler import CurrencyHandler


router = APIRouter()

@router.get("/exchange_rates/{date}", responses={200:{"model": CurrencyListResponse}}, )
async def get_exchange_rates_by_date(
    response: Response,
    date: str = Path(..., title="the specified day", description="you must pass the date in the following format: yyyy-mm-dd"),
    handler: CurrencyHandler = Depends(CurrencyHandler),
):
    """information about the exchange rate for the specified day"""
    return await handler.get_exchange_rates_by_date(date, response=response)