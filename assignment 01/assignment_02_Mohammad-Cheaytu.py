import.re # import regex

def countDigits(x): 
    if x < 10:
         return 1 
    else: 
        return 1 + countDigits(x // 10) # recursive that divide x by 10 (to remove the last digit) and add 1 to the result
def findMax(x):
    
    if len(x) == 1:
        return x[0] # if the input list have only one element, that element is the maximum value.
    else:
        y = findMax(x[:-1]) # recursive that remove the last element from the list and call findMax again with the remaining elements
        if y > x[-1]: # compare the result to the last element of the original list to see which is larger
             return findMax   # return the maximum value found.
        else:
             return x[-1]
             
def countTags(x, y):
    
    pattern = r'<{}>.*? </{}>(?:</{}>)? '.format(y, y, y) # a regex pattern to match the opening and closing tags
    
    regex = re.compile(pattern)  # compile regex pattern
    
    matches = regex.findall(x)  # find the matches in HTML string
    
    count = len(matches)  # count matches
    
    return count
def exit():
  print("You have exited the program")


def displayMenu():
  print("The Menu:\n 1. Count Digits\n 2. Find Max\n 3. Count Tags\n 4. Exit\n")



displayMenu()


def main2():
    
  displayMenu()
  
  choice = int(input("Please enter your choice here:"))


  while (choice != 4):
    if choice == 1:
      x = int(input("what is the number? "))  
      print(countDigits(x))
    elif choice == 2:
      x = input("type the numbers here with a comma between them: ").split(",")
      print(findMax(x))
    elif choice == 3:
      x = input("""write the HTML code here: """)
      y = input("what are the tags?: ")
      print(countTags(x, y))

    else:
      print("Invalid choice")

    break

  exit()



main2()
