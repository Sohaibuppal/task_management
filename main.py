from fastapi import FastAPI
from database import Base, engine
from routes.api import api_router
from routes.web import web_router

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(api_router, prefix="/api")
app.include_router(web_router)