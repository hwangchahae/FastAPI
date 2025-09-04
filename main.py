from fastapi import FastAPI 
from routers import items

app = FastAPI()

@app.get("/")
def read_root():
    return{"hello":"world"}

# 라우터 등록
app.include_router(items.router, prefix="/items", tags=["items"])
