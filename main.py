import django_setup  # noqa #isort:skip
import uvicorn
from fastapi import FastAPI

from pizzaria.router import router

app = FastAPI()
app.include_router(router, prefix="/pizzas")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
