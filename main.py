import random
from product import Product
from product_manager import ProductManager
from cart import Cart

if __name__ == "__main__":
    lista = ProductManager()
    
    
lista.add_product(Product("iPhone", 4000, 10))
lista.add_product(Product("Casti", 400, 10))
lista.add_product(Product("Incarcator", 120, 10))

print("Lista produselor:")
lista.display_products()

print(f"Valoarea inventarului: {lista.total_inventory_value()}")

cart = Cart()

select_prod = random.sample(lista.products, 2)
for product in select_prod:
    cart.add_to_cart(product)

print("Cosul contine:")
cart.display_cart()
print(f"Total {cart.calculate_total()}")