from fastapi import APIRouter
from .get_exchange_rates_by_date import router
from .get_exchange_rates import router as get_exchange_rates_router


exchange_rate_router = APIRouter(prefix="/currency", tags=["currency"])

exchange_rate_router.include_router(router)
exchange_rate_router.include_router(get_exchange_rates_router)