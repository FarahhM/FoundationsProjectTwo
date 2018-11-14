# CREATION OF DATA
######################### DO NOT MODIFY THIS CODE ###########################
from components import Store, Product

stores = []
def create_product(store, name, description, price):
    product = Product(name, description, price)
    store.add_product(product)

zara = Store("Zara")
nike = Store("Nike")
apple = Store("Apple")
stores.append(zara)
stores.append(nike)
stores.append(apple)
create_product(zara, "Nice Yellow Top", "A nice yellow top.", 30)
create_product(zara, "Pants", "100 percent cotton", 25)
create_product(nike, "Running Shoes", "Shoes for running.", 15)
create_product(nike, "Style Shoes", "Stylish shoes.", 20)
create_product(apple, "iPhone X", "256GB Space Gray", 310)
create_product(apple, "iPhone 5s", "128GB Silver", 250)

#############################################################################
# To create a new store:
    # Create a new Store() object, and append it to the stores list.
mango = Store("Mango")
stores.append(mango)
create_product(mango, "White Jeans", "Staright Cut", 22)
create_product(mango, "Blazer", "Navy plaid", 29)
# To add a new product to the store:
    # use the create_product() function
    # which takes the store you want to add the product to, and the product details
pharmacy = Store("Pharmacy")
stores.append(pharmacy)
create_product(pharmacy, "Melatonin 5mg", "50 pills", 5)
create_product(pharmacy, "Melatonin 10mg", "50 pills", 8)
