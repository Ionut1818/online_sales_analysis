from product import Product
from product_manager import ProductManager

if __name__ == "__main__":
    lista = ProductManager()
    
    
lista.add_product(Product("iPhone", 4000, 5))
lista.add_product(Product("Casti", 400, 5))
lista.add_product(Product("Incarcator", 120, 5))


