import requests
from bs4 import BeautifulSoup
import os
import json

def main2():
    greetings()
    displayMenu()

    choice = int(input("Please enter your choice here:"))

    while (choice != 9):
        if choice == 1:


        elif choice == 2:


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