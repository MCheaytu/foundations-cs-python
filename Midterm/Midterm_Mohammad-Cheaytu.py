# findings, try except else, requests, beautiful soup, List insert() method, list clear method, json.dump(), os.path.exists(),json.load(), list.copy(), Import json Module, req.get, 
import requests
from bs4 import BeautifulSoup
import os
import json

tabs = [] # List to store open tabs

# If the admin chooses (1), the system should allow the user to add a new tab by
# asking for the Title and the URL of the website.
def openTab(url, title): # Function to open a new tab
    try:
        r = requests.get(url) #  Make a request to the given url
    except:
        print("Invalid url") # If there was an error print invalid url
    else:
        tab = {"Index": len(tabs), "Title": title, "URL": url} # Create a new tab dictionnary
        tabs.append(tab) # Add it to the list
        print(tabs)
# -----------------------------------------
  
#If the admin chooses (2), the system should permit the user to input the index of the
#tab they wish to close. If no index is provided, the system will close the last opened
#tab.
  
  
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
# -----------------------------------------
  
#If the admin chooses (3), the system should enable the user to enter the index of
#the tab for displaying its content. If no index is provided, the system will display
#the content of the last opened tab. Note: 'Displaying' in this context refers to printing
#the HTML content of the URL associated with the tab. Conduct some research on
#web scraping for more insights.
  
  
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
# -----------------------------------------
#If the admin chooses (4), the system should print the titles of all open tabs. If there
#are nested tabs, display them hierarchically
  
  
def displayTabs():
    title = [i['Title'] for i in tabs] 
    print(title)
# -----------------------------------------
#If the admin chooses (5), the system should enable users to create nested tabs by
#specifying the index of the parent tab where they want to insert additional tabs
#After entering the index, the system should prompt the user to input the titles and
#contents for the new tabs.
   
   
def nestedTabs(new_tab, parent_index, url):
    nested_tab_position = parent_index + 1 # Nested tab position

    index = [i['Index'] for i in tabs]
    try:
        index == parent_index # Check if inputed value exists in tabs

    except:
        print("No such index")
    else:
        try:
            r = requests.get(url)
        except:
            print("invalid url")
        else:
            tabs.insert(nested_tab_position, new_tab) # Insert new tab at the specified position
            print(tabs)
# -----------------------------------------  
# If the admin chooses (6), the system should allow users to clear all opened tabs.
      
      
def clearTabs():
    tabs.clear() # clear tabs
    print(tabs)
# -----------------------------------------  
# If the admin chooses (7), the system should prompt the user to provide a file path as
#a parameter to save the current state of open tabs. Each tab's information, including
#title, content, and any nested tabs, should be written to the file in JSON format.
#Conduct some research for additional insights on JSON.
     
def saveTabs(path1):
    file_name = "tabs.json"
    if os.path.exists(path1):  # Check if path exists
        os.chdir(path1) # Change directory to the specified path
        with open(file_name, "w") as file_object: # Open tabs.json in write mode as a file object
            json.dump(tabs, file_object) # Dumps list tabs to tabs.json
        print("Operation done")
    else:
        print("The specified file does not exist")
# -----------------------------------------  
# If the admin chooses (8), the system should prompt the user to input a file path as a
# parameter to load tabs from the specified file.
    
def importTabs(path1):
    file_name = "tabs.json"
    if os.path.exists(path1):
        os.chdir(path1)
        with open(file_name, "r") as file_object: # Open tabs.json in read mode as a file object
            data = json.load(file_object) # Load data from tabs.json
            tabs.append(data.copy()) # add data in tabs.json to the list tabs
        print(tabs)
    else:
        print("The specified file does not exist")
# ----------------------------------------- 
        
def displayMenu():
    print("The Menu:\n 1. Open Tab\n 2. Close Tab\n 3. Switch Tab\n 4. Display All Tabs\n 5. Open Nested Tab\n 6. Clear All Tabs\n 7. Save Tab\n 8. Import Tabs\n 9. Exit\n")


def greetings():
    print("Hello, User!")
    
def main2():
    greetings()
    displayMenu()

    choice = int(input("Kindly enter your choice here: "))

    while (choice != 9):
        if choice == 1:
            url = input("Kindly Enter the URL: ") # Url value
            title = input("Kindly enter the title:")  #Title name
            openTab(url, title) # Calling the function

        elif choice == 2:
            user_input = input("Kindly enter the index number: ")
            closeTab(user_input)
            print(tabs)


        elif choice == 3:
            user_input = input("Kindly enter the index number: ")
            switchTab(user_input)

        elif choice == 4:
            displayTabs()

        elif choice == 5:
            parent_index = int(input("Kindly enter the index number: "))
            title = input("Kindly enter the title of the tab: ")
            url = input("Kindly enter the url of the tab: ")
            new_tab = {"Index": parent_index + 0.1, "Title": title, "URL": url}  # create a dictionnary out of the inputed values and adding 0.1 to the parent_index
            nestedTabs(new_tab, parent_index, url)
        elif choice == 6:
            clearTabs()

        elif choice == 7:
            path1 = input("Kindly write the file path :") # Prompting the user to add the path
            saveTabs(path1)


        elif choice == 8:
            path1 = input("Kindly write the file path :")
            importTabs(path1)

        elif choice == 9:
            exit()

        else:
            print("Invalid choice")

        displayMenu()
        choice = int(input("Kindly enter your choice here:"))
    exit()




main2()