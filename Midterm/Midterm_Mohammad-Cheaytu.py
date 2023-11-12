# findings, try except else, requests, beautiful soup
#  List insert() method, list clear method, json.dump(), os.path.exists(),json.load(), list.copy()
import requests
from bs4 import BeautifulSoup
import os
import json

tabs = [] # List to store open tabs
def openTab(url, title): # Function to open a new tab
    try:
        r = requests.get(url) #  Make a request to the given url
    except:
        print("invalid url") # If there was an error print invalid url
    else:
        tab = {"Index": len(tabs), "Title": title, "URL": url} # Create a new tab dictionnary
        tabs.append(tab) # Add it to the list
        print(tabs)
        
def closeTab(user_input): # Function to close a tab
    global tabs
    if user_input: # Check if the user provided input
        try:
            user_float = float(user_input) # Iterate over the list of dictionaries and remove the one with a matching "Index" value
            tabs = [i for i in tabs if i.get("Index") != user_float]

        except:
            print("Invalid input")
    else:
        if tabs: # If there is no index remove the last tab
            tabs.pop()

def switchTab(user_input):

    try:
        user_input is None # Check if the user didn't input a value
    except:
        int_index = int(user_input)
        r1 = requests.get(tabs[int_index]["URL"]) # Request the specified url
        doc = BeautifulSoup(r1.text, "html.parser") #print the HTML content
        print(doc.prettify())
    else:
        r2 = requests.get(tabs[-1]["URL"]) # If input is None request last tab url and show it's content
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
            
def clearTabs():
    tabs.clear()
    print(tabs)
    
def saveTabs(path1):
    file_name = "tabs.json"
    if os.path.exists(path1):
        os.chdir(path1)
        with open(file_name, "w") as file_object:
            json.dump(tabs, file_object)
        print("Operation done")
    else:
        print("The specified file does not exist")
        
def importTabs(path1):
    file_name = "tabs.json"
    if os.path.exists(path1):
        os.chdir(path1)
        with open(file_name, "r") as file_object:
            data = json.load(file_object)
            tabs.append(data.copy())
        print(tabs)
    else:
        print("The specified file does not exist")
    
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
            clearTabs()

        elif choice == 7:
            path1 = input("kindly write the file path :")
            saveTabs(path1)


        elif choice == 8:
            path1 = input("kindly write the file path :")
            importTabs(path1)

        elif choice == 9:
            exit()

        else:
            print("Invalid choice")

        displayMenu()
        choice = int(input("Please enter your choice here:"))
    exit()




main2()