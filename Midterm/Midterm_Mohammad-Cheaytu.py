import requests
from bs4 import BeautifulSoup
import os
import json

tabs = []
def openTab(url, title):
    try:
        r = requests.get(url)
    except:
        print("invalid url")
    else:
        tab = {"Index": len(tabs), "Title": title, "URL": url}
        tabs.append(tab)
        print(tabs)
        
def closeTab(user_input):
    global tabs
    if user_input:
        try:
            user_float = float(user_input)
            tabs = [i for i in tabs if i.get("Index") != user_float]

        except:
            print("Invalid input")
    else:
        if tabs:
            tabs.pop()


def main2():
    greetings()
    displayMenu()

    choice = int(input("Please enter your choice here:"))

    while (choice != 9):
        if choice == 1:
            url = input("Enter the URL: ")
            title = input("Plz enter the Title:")
            openTab(url, title)

        elif choice == 2:
            user_input = input("Please enter the index number: ")
            closeTab(user_input)
            print(tabs)


        elif choice == 3:


        elif choice == 4:


        elif choice == 5:

        elif choice == 6:


        elif choice == 7:

        elif choice == 8:


        elif choice == 9:
            exit()

        else:
            print("Invalid choice")

        displayMenu()
        choice = int(input("Please enter your choice here:"))
    exit()




main2()