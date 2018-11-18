# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.ShopNow.com"  

def welcome():
    print("Welcome to %s \n These are all the available stores in our website. You can checkout only once!: " %site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    for store in stores: 
        print("- %s" % store.name)

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    for store in stores:
        if store_name.lower() == store.name.lower():
            return store
    return False
        

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    
    print_stores()
    store_name= input('Pick a store by typing its name. Or type "checkout" to pay your bills and say your goodbyes.\n')
   
    
    while store_name.lower()!="checkout":

        
        picked_store=get_store(store_name)
        if picked_store==False:
            print("There's no available store with that name. Please try again.")
            store_name=input()
        else:
            return picked_store
    return "checkout"       
    
    
        
def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    #picked_store.print_products()
    your_choice=input("Pick the items you would like to add in your cart by following the exact spelling.\n Type 'back' to go back to the main menu where you can checkout\n")
    while your_choice.lower() != "back":
        
        for product in picked_store.products:
            if your_choice.lower() == product.name.lower():
                cart.add_to_cart(product)
                your_choice=input()
                   


def shop():
    """
    The main shopping functionality
    """
    #you need to loop here!!
    
    cart = Cart()
    cond=True
    
    while cond:
        picked_store=pick_store()
        if picked_store== "checkout":
        #cart.checkout()  
            cond=False
            #break 
        else:
            picked_store.print_products()
            pick_products(cart,picked_store)
    cart.checkout()
     

def thank_you():
    print("Thank you for shopping with us at: %s" % site_name)
