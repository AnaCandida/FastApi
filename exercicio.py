from typing import Optional, Union
from fastapi import FastAPI, Header
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    descricao: str
    valor: float
    quantidade: int


app = FastAPI()

items = []


@app.get("/")
def read_root(user_agent: Optional [str] = Header(None)):
    return {"user_agente": user_agent}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in items:
        if item_id == item.id:
            return {
                "id": item.id,
                "descricao": item.descricao,
                "valor": item.valor,
                "quantidade": item.quantidade
            }


@app.get("/items")
def read_all_items():
    return items

@app.post("/item")
def add_item(novo_item:Item):

    items.append(novo_item)

    return novo_item
 