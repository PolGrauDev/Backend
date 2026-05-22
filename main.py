from fastapi import FastAPI
from typing import TypedDict

app = FastAPI()

class BubbleTea(TypedDict):
    id: int
    name: str
    precio: float
    temperature: str
    active: bool

bubbles: list[BubbleTea] = [
    {"id":1, "name": "Matcha Latte","precio": 6.5, "temperature": "templado", "active": True},
    {"id":2, "name": "Té Negro con leche", "precio": 5.65, "temperature": "caliente", "active": True},
    {"id":3, "name": "Té rojo con tapioca", "precio": 6, "temperature": "frio", "active": False},
    {"id":4, "name": "Leche manchada", "precio": 5.65, "temperature": "caliente", "active": True}
]

@app.get("/bubbles")
def get_bubbles() -> list[BubbleTea]:
    return get_bubbles_filtered()

def get_bubbles_filtered() -> list[BubbleTea]:
    return [bubble for bubble in bubbles if bubble["active"]]