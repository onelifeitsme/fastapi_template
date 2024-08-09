from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_iddd}")
async def read_item(item_iddd: int):
    print(item_iddd)
    return {"item_id": item_iddd}
