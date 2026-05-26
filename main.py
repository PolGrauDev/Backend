from fastapi import FastAPI

from routes.bubbletea import router as bubbletea_router

app = FastAPI()

app.include_router(bubbletea_router)