from fastapi import FastAPI

app=FastAPI()

@app.get("/products")
def read_products():
    return{
        "action": "read all products"
}

@app.post("/products")
def create_product():
    return{
        "action": "create a new product"
}

@app.put("/products/1")
def read_product():
    return{
        "action": "replace All details of product with id 1"
}

@app.patch("/products/1")
def update_product():
    return{
        "action": "update PART of product 1"
}


@app.delete("/products/1")
def delete_product():
    return{
        "action": "delete product 1"
}