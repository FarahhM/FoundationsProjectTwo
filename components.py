# CLASSES AND METHODS
class Store():
    
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        self.name=name
        self.products=[]
    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        #self.product=product
        
        self.products.append(product)

    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        print("-----------------------------------")
        print("%s: \n" % self.name) 
        for product in self.products:
            print("%s \n" % product)



class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        self.name=name
        self.description=description
        self.price=price

    def __str__(self):
        return "\tProduct name: %s\n \tProduct description: %s\n \tProduct price: %s KD \n" %(self.name, self.description, self.price)


class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        self.products=[]

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        #self.product=product
        self.products.append(product)

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        price=0
        for product in self.products:
            price+=product.price
        return price
        

    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        print("-----------------------------------")
        print("Your detailed receipt will be:\n")
        for product in self.products:
            print(product)
        print("your total price will be: \n %s KD" % self.get_total_price())


    def checkout(self):
        """
        Does the checkout.
        """
        self.print_receipt()
        choice= input("Would you like to confirm? \n Y:for yes N:for no \t")
        if choice =="y" or choice == "Y":
            self.products=[]
            print("Your order has been placed")
        elif choice == "n" or choice == "N":
            print("Your order has been canceled")
