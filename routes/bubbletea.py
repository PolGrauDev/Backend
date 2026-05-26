from fastapi import APIRouter
from typing import Any

router = APIRouter()

from models.bubbletea import BubbleTea
from utils.dbconection import get_connection


@router.get("/")
def saludo() -> None:
    return {"message": "Hello WORLD!"}

@router.get("/bubblesAiven")
def get_bubbles_aiven() -> dict:
    try:
        con = get_connection()
        with con.cursor() as cur:
            cur.execute("SELECT * FROM bubble_tea")
            row = cur.fetchall()
        return{"ok": True, "result": row}
    
    except Exception as e:
        return {"ok": False, "detail": str(e)}

@router.get("/bubblesAiven/{id}")
def get_bubbles_aiven_id(id: int) -> dict:
    try:
        con = get_connection()
        with con.cursor() as cur:
            querry = "SELECT * FROM bubble_tea WHERE id_bubble_tea = %s"
            cur.execute(querry, (id,))
            row = cur.fetchone()
        return{"ok": True, "result": row}
    
    except Exception as e:
        return {"ok": False, "detail": str(e)}
    
@router.post("/bubblesAiven")
def create_bubble(bubbletea: BubbleTea):
    try:
        con = get_connection()
        with con.cursor() as cur:
            cur.execute(
                "INSERT INTO bubble_tea (bubble_name, bubble_price, bubble_temperature, bubble_active) VALUES (%s, %s, %s, %s)",
                (bubbletea["name"], bubbletea["precio"], bubbletea["temperature"], bubbletea["active"])
            )
            con.commit()


        return{"ok": True, "result": bubbletea}
    except Exception as e:
        return {"ok": False, "detail": str(e)}
    
@router.put("/bubblesAiven/{id}")
def soft_delete(id: int):
    try:
        con = get_connection()
        with con.cursor() as cur:
            query = "UPDATE bubble_tea SET bubble_active = 0 WHERE id_bubble_tea = %s"
            cur.execute(query, (id,))
            con.commit()
        
        return{"ok": True, "message": f"Bubble tea con ID {id} desactivado correctamente"}

    except Exception as e:
        return {"ok": False, "detail": str(e)}



