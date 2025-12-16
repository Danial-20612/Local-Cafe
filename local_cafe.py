import json
import bcrypt
import unittest
import tkinter as tk
from tkinter import messagebox

# while loop 
while True: # while loop runs the loop at start to fulfil a condition

    # function to load users
    def loading_users_json(): # function to loading users from json file
        # open function
        with open("users.json", "r") as f:  # this loads the users.json file as "read" mode
            # return function
            return json.load(f) # returning data
        
    # function
    def saving_users_json(data): # this will write the new users using "w" mode
        with open("users.json", "w") as d: # opening file as d
            json.dump(data, d, indent=4) # dumping the file

    # function for appending
    def appending_user_json(name, username, password): # this will add users using 3 parametre 
        users = loading_users_json() # variable for strong users in json
        # Hashing the passwords before strong
        passwrod_hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()) # this command convert passwwrd to hash
        users["users"].append({ # linking the json file to append new users
            "name": name,
            "username": username,
            "password": passwrod_hashed.decode("utf-8")  # store as string
        })
        saving_users_json(users) # sotred to json new users

    # function for verifying 
    def validating_user_detials(username, password): # validating new credentials
        customers = loading_users_json() # customers variable stores json file data
        for user in customers["users"]: # for each user in json file 
            if user["username"] == username: # username will be stored here
                stored_hash = user["password"].encode("utf-8") # decodes password
                return bcrypt.checkpw(password.encode("utf-8"), stored_hash) # returning the password from json
        return False # this will return false if the validation failed

    # print function
    print("Welcome to Local Cafe Account Page : ")
    # user input
    if_account_exsists = input("Do you have an account YES/NO: ")
    if_account_exsists = if_account_exsists.upper()

    if if_account_exsists == "YES": # if statment to check user response
        break # if the user have accont it will break and move on

    else:  # else statment
        print("You dont have an account . Simply make an account: ") # print function
        customer_name = input("Enter your name: ") # input customer name
        username = input("Enter your username: ") # input username
        Password = input("Enter your password please: ") # password for input
        # Example usage
        appending_user_json(customer_name, username, Password) # appending user from prevous inputs
        break 


# log in simulation
print("--" * 56) # creates a simple seperator
print("You now have created an account,  log in please: ") # print function
customer_username = input("Enter your username: ") # user input
customer_password = input("Enter your password: ") # user input
print(validating_user_detials( customer_username, customer_password ))  # True / OR 





#-------------------------------------------------------------CLEARED----------------------------------------------------------------------

print("Greetings: Local Cafe Homepage ordering system: ")

# class Inventory menu
class Inventory_Menu: # parent class for foods and drinks
    def __init__(self, name, price, category): # init constructors creates items objects
        # reinisialisation
        self.name = name
        self.price = price
        self.next = None   
        self.category = category

    def __str__(self): # function that accepts str
        return "{} ({}) - £{}".format(self.name, self.category, self.price) # return function to we can access content

# class munu food
class Menu_Food(Inventory_Menu): # holds food list in it
    def __init__(self, name, price): # constructor to create and store food items
        super().__init__(name, price, "Menu Food") # super function sends the arguments to parent init constructor

# class for drinks
class Menu_Drink(Inventory_Menu): # inherits all from parent class 
    def __init__(self, name, price): # recieves name and price of each drink item
        super().__init__(name, price, " Menu Drink") # menu drink is passing these arguments to parent class

# Menu for the local cafe 
class Menu_Items: # class for all the available foods and drinks from the local cafe
    def __init__(self): # function to construct the menu list
        # below is all what is available 
        self.items = [
            Menu_Food("Pizza", 22),
            Menu_Food("Burger", 4.50),
            Menu_Food("Pasta" , 5.10),
            Menu_Food("Fish and Chips" , 10),
            Menu_Food("Panini", 8),
            Menu_Drink("Pepsi", 3),
            Menu_Drink("Tango", 2.75),
            Menu_Drink("Water", 1),
            Menu_Drink("Hot Chocolate", 2.70),
            Menu_Drink("Sprite", 4)
        ] # the above block of code is mutable

# class Munu order
class Menu_Order: # oders gets info from users 
    def __init__(self): # self is the current object
        self.cart = []  # empty array for storing User preferences

    def appending_item(self, item): # appends the selected items to cart function
        self.cart.append(item)

    # def function called emptying cart
    def emptying_cart(self): # it selects objects in cart
        self.cart.clear() # this command simply destroys the cart content

    # def function for displaying selected items
    def display_cart_items(self): # function for displaying cart to user
        if not self.cart: # if there is nothing selected it will return see below
            return "Your cart  has nothing [EMPTY]: " # this line will print
        text = "🛒 Your Cart 🛒 \n" # this is the visual user will see for cart 
        for i, item in enumerate(self.cart, 1): # this will provide both index and value in a loop 
            text += "{}. {}\n".format(i, item) # this will simply add and appen selections
        return text # return the cart content in text variable

# class bill
class Bill: # for strong the price
    def __init__(self, order): # two parametre to store oder info
        self.order = order # re-initialising self.order 

    def total(self): # def function to display to user the total amount depending on what they selected and how many
        return sum(i.price for i in self.order.cart) # this command simply returns the total price within the cart prtal

# class called end users
class End_Users:
    def __init__(self, name): # this will assingt user name 
        self.name = name  # initialising self.name 
        self.order = Menu_Order() # == calling the class Menu order to set for self.order


# TKINTER Module-------------------
# TKINTER for graphical user interface contains widgets and buttons and icons rather then interacting with terminal
# def function for running gui
def running_tkinter_gui(menu, customer): # has two parametre called menu and customer
    root = tk.Tk() # == normal variable called root to initailte the window
    root.title("The Local Cafe Order Food & Drink for Loved ones: 💖 ") # assigning the title of the windows
    bill = Bill(customer.order) # bill variable by calling Bill class and sending customer.order
    

    # Listbox to show menu items
    listbox = tk.Listbox(root, width=60) # setting up the width 
    for item in menu.items: # for loop to extract all menu items
        listbox.insert(tk.END, str(item)) # this command will insert each item to the empty box
    listbox.pack() # packs all the buttons and widget into root variable windows
    # def function for appening to cart
    def appending_toCart(): # this will add items to cart in gui
        selection = listbox.curselection() # stores the selected items to listbox
        if selection: # if statment
            customer.order.appending_item(menu.items[selection[0]]) # this commands appends the item to the end
            messagebox.showinfo("Inserted", "Your Item added to your cart.") # = display message for conformation
    # function to view the cart 
    def view_cart_total(): # displays the cart into gui as widget
        selection = customer.order.display_cart_items() # calling the function to display items selection
        billing = bill.total() # variable called billing to strore total bil cost
        # messagebox
        messagebox.showinfo("Order Summary", "{}\nTotal: £{}".format(selection, billing)) # dispays this oder summary and total
    # this for destroying the cart
    def emptying_cart(): # deletes everything from the cart in gui 
        customer.order.emptying_cart() # this function is used for that
        messagebox.showinfo("Cart", "Your Cart is EMPTIED: ") # display message 
    
    # def function for close
    def close_windows(): # this will simply close the gui windows
        if root.winfo_exists(): # if statment to check if is opened then it will destroy upon calling/ pressing button
            # Example close button
            root.destroy() # this commands renders the gui windows
    # clearing cartfunction
    def emptying_cart(): # this def function will simply used for deleting all the selected items
        customer.order.emptying_cart() # = calling the function to delete content
        messagebox.showinfo("Cart", "Your Cart is EMPTIED: ") # message box for displaying the message
        
    # def function for close
    def close_windows(): # this will simply close the gui windows
        root.destroy() # this commands renders the gui windows

    # bwlow is the block of code for using the def function see above into buttons for each functionality

    tk.Button(root, text=" ➕ Add Selected", command=appending_toCart).pack(pady=5)  # button 1
    tk.Button(root, text=" 🛒 Show Cart & Total 💵 ", command=view_cart_total).pack(pady=5) # button 2
    tk.Button(root, text=" ➖ Clear Cart", command=emptying_cart).pack(pady=5) # button 3
    tk.Button(root, text=" ✖️ Click here to Pay: ", command=close_windows).pack(pady=5) # button 4
    tk.Button(root, text=" ✖️ Close the Windows", command=close_windows).pack(pady=5) # button 5

    
    # running the gui
    root.mainloop() # root= tk.TK() will instantiate the window object but root.mainloop will keep it responsive and opened.


# == the below code will initialise and run the entire code and TKINTER gui interface

menu = Menu_Items() # creating object of calss Menu items
customer = End_Users("Danial")
running_tkinter_gui(menu, customer)


###############################################################END################################################################








