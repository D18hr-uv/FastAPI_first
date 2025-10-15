from fastapi import FastAPI
from models import Product


app = FastAPI()

@app.get("/")
def greet():
    return "Hello ji"

products = [
    Product(id = 1,name = "phone", description= "budget phone", price= 99.99, quantity= 10),
    Product(id = 2,name = "laptop", description= "budget laptop", price= 999.99, quantity= 5),
    Product(id = 3,name = "tablet", description= "budget tablet", price= 199.99, quantity= 20)
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product(id: int):
    for product in products:
        if product.id == id:
            return product
        
    return {"error": "Product not found"}

@app.post("/product")
def add_product(product: Product):
    products.append(product)


@app.put("/product")
def update_product(id:int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product Updated Successfully"
    return "Sorry! It didn't work"


@app.delete("/product")
def delete_product(id:int):
    for i in range (len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted"
    return "Sorry! It didn't work"

# To run this FastAPI application, you need to use Uvicorn.
# 1. Make sure you have uvicorn installed: pip install "uvicorn[standard]"
# 2. Run the application from your terminal in the directory where main.py is located:
#    uvicorn main:app --reload
# 3. Then open your browser to http://127.0.0.1:8000/
# 4. For interactive API documentation, go to http://127.0.0.1:8000/docs
