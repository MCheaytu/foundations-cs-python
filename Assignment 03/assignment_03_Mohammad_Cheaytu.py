data = [ {
"ID": 1,
"Name": "Ali",
"Age": 22,
"Major": "Computer Science",
"GPA": 3.7
},
{
"ID": 2,
"Name": "Bouchra",
"Age": 21,
"Major": "Engineering",
"GPA": 3.9
}
]
# Choice 1: This function takes the student data and a student's ID as arguments and returns the
#information of the student with the given ID

def studentId(x):
    if x <= 2 and x > 0: # see if the id inputed is either 1 or 2 
        y = [data[x-1]["ID"], data[x-1]["Name"], data[x-1]["Age"], data[x-1]["Major"],data[x-1]["GPA"] ] # get the value of the keys 
        return y
    else:
      print("Student not found")
# -----------------------------
# Choice 2: This function takes the student data as an argument and returns a list of all students'
#information.

def getAllStudent():
    return data
# -----------------------------

#Choice 3: This function takes the student data and a major as arguments and returns a list of
#students in the specified major.

def studentMajor(x):
    sentence_1 = "Computer Science" 
    sentence_2 = "Engineering"
    if x == sentence_1: 
        dic_1 = data[0] # assigning the first element in the list to a variable
        list_1 = list(dic_1.values()) # take the values of the keys in the first element and covert them to a list
        print(list_1)
    elif x == sentence_2:
        dic_2 = data[1]
        list_2 = list(dic_2.values())
        print(list_2)
    else:
        print("student of the major were found")
# -----------------------------
