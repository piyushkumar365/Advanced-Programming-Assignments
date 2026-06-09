# Default products (5 already added)
products = [
    {"name": "Pen", "stock": 25},
    {"name": "Notebook", "stock": 8},
    {"name": "Pencil", "stock": 5},
    {"name": "Eraser", "stock": 12},
    {"name": "Marker", "stock": 3}
]

# Ask user how many more products to add
n = int(input("How many more products do you want to add? "))

for i in range(n):
    print(f"\nEnter details for product {i+1}:")
    name = input("Product name: ")
    stock = int(input("Stock quantity: "))
    products.append({"name": name, "stock": stock})

# Display products with stock less than 10
print("\nProducts with stock less than 10:\n")

for product in products:
    if product["stock"] < 10:
        print(f"Product Name: {product['name']}, Stock: {product['stock']}")
