from pprint import pprint

from fastapi import FastAPI
import sys
from pathlib import Path

# Получаем корневую директорию проекта (на уровень выше директории app)
# project_root = Path(__file__).resolve().parent.parent
# sys.path.insert(0, str(project_root))
#
#
pprint(sys.path)
from routers.product import router as product_router


app = FastAPI()
app.include_router(product_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
