def getFactorial():
    x = int(input("what is the number? "))
    if x < 0:
        return False
    elif x < 2:
        return 1
    else:
        for i in range(1, x):
           x *= i
        return x
     


print(getFactorial())

# ------------------

def fun():
  x = int(input("give me the integer!"))
  y = []

  for i in range(1, x // 2): 
    # divise integer by 2 cause the result will be the same
    if x % i == 0:
      y.append(i)
  return y

print(fun())

# -------------

def reverseString():
    x = str(input("type your string here"))
    y = ""
    for i in x:
        print(i)
         
    print(y)
    
          

reverseString()
