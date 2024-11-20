from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from sqlalchemy import select, insert

from models.models import InsuranceRate
from rate.schemas import Rate, RatesInput, Insurancerate

router = APIRouter()

@router.get("/", summary="Получить всё из таблицы InsuranceRate", response_model=list[Insurancerate])
async def get_rate(session : AsyncSession = Depends(get_async_session)):
    query = select(InsuranceRate)
    result = await session.execute(query)
    return result.all()


@router.post("/load-rates", summary="Загрузить тарифы") 
async def load_rates(rates: RatesInput, session : AsyncSession = Depends(get_async_session)): 
    async with session.begin():
        for rate_date, rate_items in rates.root.items():
            for rate_item in rate_items:
                data = { "date": rate_date, "cargo_type": rate_item.cargo_type, "rate": rate_item.rate }
                query = insert(InsuranceRate).values(**data) 
                await session.execute(query)
    await session.commit()
    return {"message": "тарифы загружены"}
    


@router.post("/insurance", summary="Узнать стоимость страхования")
async def calculate_insurance(request: Rate, session : AsyncSession = Depends(get_async_session)):
    query = select(InsuranceRate.c.rate).filter(InsuranceRate.c.date == request.date, InsuranceRate.c.cargo_type == request.cargo_type)
    result = await session.execute(query)
    rate = result.scalar()
    if not rate: 
        raise HTTPException(status_code=404, detail="Rate not found")
    insurance_cost = request.declared_value * float(rate)
    return {"Стоимость страхования": insurance_cost}
