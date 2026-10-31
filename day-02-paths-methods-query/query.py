from fastapi import FastAPI, HTTPException

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "price": 1200, "in_stock": True},
    {"id": 2, "name": "Mouse", "price": 25, "in_stock": True},
    {"id": 3, "name": "Monitor", "price": 300, "in_stock": False},
]


# path parameter: একটা নির্দিষ্ট product
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


# query parameter: তালিকা ছাঁকা
@app.get("/products")
def list_products(in_stock: bool | None = None, max_price: int = 10000):
    result = []
    for product in products:
        if in_stock is not None and product["in_stock"] != in_stock:
            continue
        if product["price"] > max_price:
            continue
        result.append(product)
    return result