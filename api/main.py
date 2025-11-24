from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from routes import (company, local, vehicle, driver, employee,
                    car_model, category, ocurrence, accident, damage, line,
                    maintenance, maintenance_service, service, travel, itinerary)
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
app.include_router(employee.router)
app.include_router(local.router)
app.include_router(ocurrence.router)
app.include_router(vehicle.router)
app.include_router(driver.router)
app.include_router(car_model.router)
app.include_router(category.router)
app.include_router(accident.router)
app.include_router(damage.router)
app.include_router(line.router)
app.include_router(maintenance.router)
app.include_router(maintenance_service.router)
app.include_router(service.router)
app.include_router(line.router)
app.include_router(itinerary.router)
app.include_router(travel.router)
