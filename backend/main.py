from typing import Union
from fastapi import FastAPI
from item import Item, items

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware 
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World cosc381!!!!!! CICD ROCKS"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {
        "item_id": item_id,
        "q": "hello"
    }
# http://localhost:8000/items/1?q=abc

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {
        "item_name": item.name,
        "item_id": item_id,
        "item_price": item.price,
        "item_is_offer": item.is_offer
    }

@app.post("/items/")
def post_item(item: Item):
    # Create a new Item in the server
    item_id = 1000
    new_item = Item(item.name, item.price, item.is_offer)
    items.append(new_item)
    return {
        "item_name": item.name,
        "item_id": item_id,
        "item_price": item.price,
        "item_is_offer": item.is_offer
    }