from fastapi import APIRouter, Path, Depends
from .response_schema import CurrencyListResponse
from ..handlers.currency.currency_handler import CurrencyHandler


router = APIRouter()

@router.get("/exchange_rates/{date}", responses={200:{"model": CurrencyListResponse}})
async def get_exchange_rates_by_date(
    date: str = Path(..., title="the specified day"),
    handler: CurrencyHandler = Depends(CurrencyHandler)
):
    """information about the exchange rate for the specified day"""
    return await handler