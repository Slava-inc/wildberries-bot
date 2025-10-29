from fastapi import FastAPI

app = FastAPI()

@app.get("/api/nm")
async def mock_wb_card(nm: str):
    return {
        "data": {
            "products": [
                {
                    "id": nm,
                    "name": "Тестовый товар",
                    "price": 1000,
                    "stock": 50
                }
            ]
        },
        "success": True
    }