from pydantic import BaseModel

from pizzaria.models import TamanhoPizza


class PizzaInSchema(BaseModel):
    sabor: str
    tamanho: TamanhoPizza

    class Config:
        orm_mode = True


class PizzaSchema(PizzaInSchema):
    id: int
