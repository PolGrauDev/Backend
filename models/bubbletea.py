from typing import NotRequired, TypedDict

class BubbleTea(TypedDict):
    id: NotRequired[int]
    name: str
    precio: float
    temperature: str
    active: bool