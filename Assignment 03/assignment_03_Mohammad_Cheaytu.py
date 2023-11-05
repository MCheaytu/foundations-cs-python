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