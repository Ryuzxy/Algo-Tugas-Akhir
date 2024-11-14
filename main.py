import os
import datetime as dt
import pandas as pd
import numpy as np


date = dt.datetime.now()
print(date)

def login():
    os.system("cls")
    print("Enter your username and password")
    username = input("Username: ")
    password = input("Password: ")
    if username == "admin" and password == "admin":
        os.system("cls")
        print("Login successful")
        return True
    else:
        os.system("cls")
        print("Login failed")
        return False

def main_menu():
    os.system("cls")
    print("Main Menu")
    print("1. Add new item")
    print("2. View items")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

def add_item():
    os.system("cls")
    print("Add new item")
    item_name = input("Enter item name: ")
    item_price = float(input("Enter item price: "))
    item_quantity = int(input("Enter item quantity: "))    
    return item_name, item_price, item_quantity

def view_items():
    os.system("cls")
    print("View items")
    df = pd.read_csv("items.csv")
    print(df)
    input("Press enter to continue")

def exit_program():
    os.system("cls")
    print("Exiting program")    
    exit()

if __name__ == "__main__":
    while True:
        if login():
            while True:
                choice = main_menu()
                if choice == "1":
                    item_name, item_price, item_quantity = add_item()
                    with open("items.csv", "a") as f:
                        f.write(f"{item_name},{item_price},{item_quantity}\n")
                elif choice == "2":
                    view_items()
                elif choice == "3":
                    exit_program()
                else:
                    print("Invalid choice")
        else:
            exit_program()
        input("Press enter to continue")
        os.system("cls")
    input("Press enter to continue")
    os.system("cls")
    exit()
