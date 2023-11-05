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
# Choice 4: This function takes the student data, a name, an age, a major, and a GPA as arguments
# and adds a new student to the data.


def addStudent(x):
    data.append(x)
# -----------------------------

#Choice 5 This function takes two student data lists as arguments and returns a set of common
#majors found in both lists.


def findCommonMajor(a, b): 
  x = set(i["Major"] for i in a) # set containing the key "Major" value in list a
  y = set(i["Major"] for i in b) 
  z = x.intersection(y) # intersection result between x and y
  return z
# -----------------------------
# Choice 6: This function takes the student data and a student's ID as arguments and removes the
#student with the given ID from the data.


def deleteStudent(id):
    if data[0]["ID"] == id:
      del data[0] # delete the first element of data if the inputed id had the same value the key "ID" in the first dictionnary 
      print("The Operation completed successfully")
      print(data)
    elif data[1]["ID"] == id:
      del data[1]
      print("The Operation completed successfully")
      print(data)
    else:
      print("There is no student found with such ID")
# -----------------------------

#Choice 7: This function takes the student data as an argument and returns the average GPA of
#all the students in the data.

def calculateAverage():
    avg_gpa = (data[0]["GPA"] + data[1]["GPA"]) / 2 # combining the two GPA values and divinding them b the nb of of students which is 2 in this case
    return avg_gpa
# -----------------------------

#Choice 8: This function takes the student data and the number of top-performing students to
#retrieve as arguments. It returns a tuple of the specified number of students with the highest
#GPAs (the tuple should have the name of those students).

def getToPerformers(data):
  tuple1 = () # create an empty tuple
  data_sort = sorted(data, key=lambda x: -x["GPA"]) #sort data from the highest GPA to the lowest
  tuple2 = (*tuple1, data_sort[0]["Name"]) # add the first name value with highest GPA to the tuple
  return tuple2
# -----------------------------

# Choice 9: This choice terminates the program.

def exit():
  print("You have exited the program")