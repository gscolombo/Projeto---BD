from fastapi import FastAPI
from routes import company, worker

app = FastAPI()

app.include_router(company.router)
app.include_router(worker.router)
