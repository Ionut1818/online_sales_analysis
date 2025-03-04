from product import Product
from product_manager import ProductManager

if __name__ == "__main__":
    lista = ProductManager()
    
    
lista.add_product(Product("iPhone", 4000, 10))
lista.add_product(Product("Casti", 400, 10))
lista.add_product(Product("Incarcator", 120, 10))

print("Lista produselor:")
lista.display_products()

print(f"Valoarea inventarului: {lista.total_inventory_value()}")
