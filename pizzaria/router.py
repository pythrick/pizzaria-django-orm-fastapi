from typing import List

from fastapi import APIRouter
from pydantic import parse_obj_as

from pizzaria.models import Pizza
from pizzaria.schemas import PizzaInSchema, PizzaSchema

router = APIRouter()


@router.get("/")
def list_pizzas():
    return parse_obj_as(List[PizzaSchema], list(Pizza.objects.all()))


@router.post("/")
def create_pizza(pizza: PizzaInSchema):
    pizza = Pizza.objects.create(**pizza.dict())
    return PizzaSchema.from_orm(pizza)
