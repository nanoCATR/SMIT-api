from dotenv import load_dotenv
from fastapi import FastAPI
from rate import router as rate_router

load_dotenv()
app = FastAPI()

app.include_router(rate_router.router, prefix="/rate", tags=["rate"])
