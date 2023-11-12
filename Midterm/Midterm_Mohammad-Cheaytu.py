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

def switchTab(user_input):

    try:
        user_input is None
    except:
        int_index = int(user_input)
        r1 = requests.get(tabs[int_index]["URL"])
        doc = BeautifulSoup(r1.text, "html.parser")
        print(doc.prettify())
    else:
        r2 = requests.get(tabs[-1]["URL"])
        doc = BeautifulSoup(r2.text, "html.parser")
        print(doc.prettify())

def displayTabs():
    title = [i['Title'] for i in tabs]
    print(title)
    
def nestedTabs(new_tab, parent_index, url):
    nested_tab_position = parent_index + 1

    index = [i['Index'] for i in tabs]
    try:
        index == parent_index

    except:
        print("No such index")
    else:
        try:
            r = requests.get(url)
        except:
            print("invalid url")
        else:
            tabs.insert(nested_tab_position, new_tab)
            print(tabs)
    
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
            user_input = input("Please enter the index number: ")
            switchTab(user_input)

        elif choice == 4:
            displayTabs()

        elif choice == 5:
            parent_index = int(input("Kindly enter the index number: "))
            title = input("Kindly enter the title of the tab: ")
            url = input("kindly enter the url of the tab: ")
            new_tab = {"Index": parent_index + 0.1, "Title": title, "URL": url}
            nestedTabs(new_tab, parent_index, url)
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