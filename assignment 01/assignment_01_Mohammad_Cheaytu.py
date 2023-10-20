 #Nb 1
def getFactorial():
    x = int(input("what is the number? "))
    if x < 0:
        return False  # if the nb is negative dont accept it
    elif x < 2:
        return 1 # if x is 1 or 0 return 1
    else:
        for i in range(1, x):
           x *= i # where the magic happens :p
        return x
     


print(getFactorial())
# ------------
#Nb 2
def divisor():
    x = int(input("type the number: "))
    y=[] # create a variable that is an empty string
    for i in range(1, x + 1):
        if x % i == 0: # divise user input with i and see if the reminder is zero
            y.append(i) # add i inside y 
    return y        
       
print(divisor())

# -------------
#Nb 3
def reverseString():
    x = str(input("type your string here: "))
    y = "" # make a variable that is an empty string
    for i in x:
        y = i + y # add char in i to the empty string
    print(y)               

reverseString()

# ------------------
#Nb 4
def fun():
  x = int(input("give me the integer!"))
  y = []

  for i in range(1, x // 2): 
    # divise integer by 2 is used here cause the result will be the same 
    if x % i == 0:
      y.append(i)
  return y

print(fun())

# ------------
#Nb 5
def password():
    x = input("What is the password?: ") # take input from the user
    # default boolean value of the variables
    upper =  False 
    number = False
    lower = False
    special = False

    if len(x) < 8: # if the char inputed by the user is less then 8 then return false
       print("Weak password")
       return

    for i in x:
        j = ord(i) # ord(i) is the unicode value of i
        if  ord("A") <= j <= ord("Z"):
           upper = True
        elif ord("0") <= j <= ord("9"):
            number = True
        elif ord("a") <= j <= ord("z"):
            lower = True
        else:
            special = True

    if upper and number and lower and special == True: #if all conditions are true print Strong password 
        print("Strong password")
    else: # if one of the conditions is False print Weak password 
        print("Weak password")

password()
# ------------
# FSW Bonus Nb
def ipv4():
    x = input("what is the ip address?")
    y = x.split('.') # split the ip into four octets

    if len(y) != 4: # make sure it is 4 octets
        return False

    for i in y:
        try:
            if len(i) > 1 and i[0] == '0': # prevent an octet from starting with 0
                return False
                
            j = int(i) 

            if j < 0: # dont' allow a negative number
                return False
            if j < 0 or j > 255: # make sure the number is between 0 and 255
                return True

        except ValueError:
            return False

    return True
print(ipv4())