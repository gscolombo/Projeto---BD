from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from routes import company, worker, local
from routes.exception import CustomHTTPException

app = FastAPI()

@app.exception_handler(CustomHTTPException)
async def custom_exception_handler(req: Request, exc: CustomHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.message,
            "details": exc.details
        }
    )

app.include_router(company.router)
app.include_router(worker.router)
app.include_router(local.router)